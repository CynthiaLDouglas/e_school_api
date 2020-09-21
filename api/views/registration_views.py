from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user, authenticate, login, logout
from django.middleware.csrf import get_token

from ..models.course import Course
from ..models.registration import Registration
from ..serializers import CourseSerializer, UserSerializer, CourseReadSerializer, RegistrationSerializer
# Create your views here.
class Registrations(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class = RegistrationSerializer
    def get(self, request):
        """Index request"""
        # Get all the mangos:
        # mangos = Mango.objects.all()
        # Filter the mangos by owner, so you can only see your owned mangos
        registrations = Registration.objects.all()
        # Run the data through the serializer
        data = RegistrationSerializer(registrations, many=True).data
        return Response({ 'registrations': data })

    def post(self, request):
        """Create request"""
        # Add user to request data object
        request.data['registration']['owner'] = request.user.id
        # Serialize/create mango
        registration = RegistrationSerializer(data=request.data['registration'])
        # If the mango data is valid according to our serializer...
        if registration.is_valid():
            # Save the created mango & send a response
            registration.save()
            return Response({ 'registration': registration.data }, status=status.HTTP_201_CREATED)
        # If the data is not valid, return a response with the errors
        return Response(registration.errors, status=status.HTTP_400_BAD_REQUEST)

class RegistrationDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request, pk):
        """Show request"""
        # Locate the mango to show
        registration = get_object_or_404(Registration, pk=pk)
        # Only want to show owned mangos?
        # if not request.user.id == registration.owner.id:
        #     raise PermissionDenied('Unauthorized...')

        # Run the data through the serializer so it's formatted
        data = RegistrationSerializer(course).data
        return Response({ 'registration': data })

    def delete(self, request, pk):
        """Delete request"""
        # Locate mango to delete
        registration = get_object_or_404(Registration, pk=pk)
        # Check the mango's owner agains the user making this request
        if not request.user.role_in_school == 'TR':
            raise PermissionDenied('Unauthorized...')
        # Only delete if the user owns the  mango
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # def partial_update(self, request, pk):
    #     """Update Request"""
    #     # Remove owner from request object
    #     # This "gets" the owner key on the data['mango'] dictionary
    #     # and returns False if it doesn't find it. So, if it's found we
    #     # remove it.
    #     if request.data['course'].get('owner', False):
    #         del request.data['course']['owner']
    #
    #     # Locate Mango
    #     # get_object_or_404 returns a object representation of our Mango
    #     course = get_object_or_404(Course, pk=pk)
    #     # Check if user is the same as the request.user.id
    #     if not request.user.id == course.owner.id:
    #         raise PermissionDenied('Unauthorized, you do not own this mango')
    #
    #     # Add owner to data object now that we know this user owns the resource
    #     request.data['course']['owner'] = request.user.id
    #     # Validate updates with serializer
    #     data = CourseSerializer(course, data=request.data['course'])
    #     if data.is_valid():
    #         # Save & send a 204 no content
    #         data.save()
    #         return Response(status=status.HTTP_204_NO_CONTENT)
    #     # If the data is not valid, return a response with the errors
    #     return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
