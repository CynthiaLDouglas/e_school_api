from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user, authenticate, login, logout
from django.middleware.csrf import get_token

from ..models.course import Course
from ..serializers import CourseSerializer, UserSerializer

# Create your views here.
class Courses(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class = CourseSerializer
    def get(self, request):
        """Index request"""
        # Get all the mangos:
        # mangos = Mango.objects.all()
        # Filter the mangos by owner, so you can only see your owned mangos
        courses = Course.objects.filter(owner=request.user.id)
        # Run the data through the serializer
        data = CourseSerializer(courses, many=True).data
        return Response({ 'courses': data })

    def post(self, request):
        """Create request"""
        # Add user to request data object
        request.data['course']['owner'] = request.user.id
        # Serialize/create mango
        course = CourseSerializer(data=request.data['course'])
        # If the mango data is valid according to our serializer...
        if course.is_valid():
            # Save the created mango & send a response
            course.save()
            return Response({ 'course': course.data }, status=status.HTTP_201_CREATED)
        # If the data is not valid, return a response with the errors
        return Response(course.errors, status=status.HTTP_400_BAD_REQUEST)

class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request, pk):
        """Show request"""
        # Locate the mango to show
        course = get_object_or_404(Course, pk=pk)
        # Only want to show owned mangos?
        if not request.user.id == course.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this mango')

        # Run the data through the serializer so it's formatted
        data = CourseSerializer(course).data
        return Response({ 'course': data })

    def delete(self, request, pk):
        """Delete request"""
        # Locate mango to delete
        course = get_object_or_404(Course, pk=pk)
        # Check the mango's owner agains the user making this request
        if not request.user.id == course.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this mango')
        # Only delete if the user owns the  mango
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update Request"""
        # Remove owner from request object
        # This "gets" the owner key on the data['mango'] dictionary
        # and returns False if it doesn't find it. So, if it's found we
        # remove it.
        if request.data['course'].get('owner', False):
            del request.data['course']['owner']

        # Locate Mango
        # get_object_or_404 returns a object representation of our Mango
        course = get_object_or_404(Course, pk=pk)
        # Check if user is the same as the request.user.id
        if not request.user.id == course.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this mango')

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
