from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models.mango import Mango
from .models.course import Course
from .models.user import User
from .models.registration import Registration

class MangoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mango
        fields = ('id', 'name', 'color', 'ripe', 'owner')

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'name', 'subject', 'course_description', 'owner')

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = ('id', 'semester', 'course_name', 'student_enrolled', 'owner')

class UserSerializer(serializers.ModelSerializer):
    # This model serializer will be used for User creation
    # The login serializer also inherits from this serializer
    # in order to require certain data for login
    class Meta:
        # get_user_model will get the user model (this is required)
        # https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#referencing-the-user-model
        model = get_user_model()
        fields = ('id', 'first_name', 'last_name', 'role_in_school', 'email', 'password')
        extra_kwargs = { 'password': { 'write_only': True, 'min_length': 5 } }

    # This create method will be used for model creation
    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)

class CourseReadSerializer(CourseSerializer):
     owner = UserSerializer(read_only=True)

class RegistrationReadSerializer(RegistrationSerializer):
     course_name = CourseSerializer(read_only=True)
     student_enrolled = UserSerializer(read_only=True)
     owner = UserSerializer(read_only=True)

class UserLoginSerializer(UserSerializer):
    # Require email, password for sign in
    email = serializers.CharField(max_length=300, required=True)
    password = serializers.CharField(required=True, write_only=True)

class UserRegisterSerializer(serializers.Serializer):
    # Require email, first_name, last_name, role_in_school, password, and password_confirmation for sign up
    email = serializers.CharField(max_length=300, required=True)
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)
    role_in_school = serializers.CharField()
    password = serializers.CharField(required=True)
    password_confirmation = serializers.CharField(required=True, write_only=True)

    def validate(self, data):
        # Ensure password & password_confirmation exist
        if not data['password'] or not data['password_confirmation']:
            raise serializers.ValidationError('Please include a password and password confirmation.')

        # Ensure password & password_confirmation match
        if data['password'] != data['password_confirmation']:
            raise serializers.ValidationError('Please make sure your passwords match.')
        # if all is well, return the data
        return data

class ChangePasswordSerializer(serializers.Serializer):
    model = get_user_model()
    old = serializers.CharField(required=True)
    new = serializers.CharField(required=True)
