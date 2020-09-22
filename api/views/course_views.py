from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user, authenticate, login, logout
from django.middleware.csrf import get_token

from ..models.course import Course
from ..serializers import CourseSerializer, UserSerializer, CourseReadSerializer

# Create your views here.
class Courses(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class = CourseSerializer
    def get(self, request):
        """Index request"""
        # Get all the courses:
        # courses = Course.objects.all()
        # Filter the courses by owner, so you can only see your owned courses
        courses = Course.objects.all()
        # Run the data through the serializer,
        # used CourseReadSerializer to include owner info
        data = CourseReadSerializer(courses, many=True).data
        return Response({ 'courses': data })

    def post(self, request):
        """Create request"""
        # Add user to request data object
        request.data['course']['owner'] = request.user.id
        # Serialize/create course
        course = CourseSerializer(data=request.data['course'])
        # If the course data is valid according to our serializer...
        if course.is_valid():
            # Save the created course & send a response
            course.save()
            return Response({ 'course': course.data }, status=status.HTTP_201_CREATED)
        # If the data is not valid, return a response with the errors
        return Response(course.errors, status=status.HTTP_400_BAD_REQUEST)

class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request, pk):
        """Show request"""
        # Locate the course to show
        course = get_object_or_404(Course, pk=pk)
        # Only want to show owned courses?
        # if not request.user.id == course.owner.id:
        #     raise PermissionDenied('Unauthorized, you did not create this course.')
        # Run the data through the serializer so it's formatted
        data = CourseReadSerializer(course).data
        return Response({ 'course': data })

    def delete(self, request, pk):
        """Delete request"""
        # Locate course to delete
        course = get_object_or_404(Course, pk=pk)
        # Check the course's owner against the user making this request
        # if not request.user.id == course.owner.id:
        #     raise PermissionDenied('Unauthorized, you do not own this course')
        # Not using line 63
        data = CourseReadSerializer(course).data
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update Request"""
        # Remove owner from request object
        # This "gets" the owner key on the data['course'] dictionary
        # and returns False if it doesn't find it. So, if it's found we
        # remove it.
        if request.data['course'].get('owner', False):
            del request.data['course']['owner']

        # Locate Course
        # get_object_or_404 returns a object representation of our Course
        course = get_object_or_404(Course, pk=pk)
        # Check if user is the same as the request.user.id
        if not request.user.id == course.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this course')

        # Add owner to data object now that we know this user owns the resource
        request.data['course']['owner'] = request.user.id
        # Validate updates with serializer
        data = CourseSerializer(course, data=request.data['course'])
        if data.is_valid():
            # Save & send a 204 no content
            data.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        # If the data is not valid, return a response with the errors
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
