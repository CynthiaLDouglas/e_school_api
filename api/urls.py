from django.urls import path
from .views.mango_views import Mangos, MangoDetail
from .views.course_views import Courses, CourseDetail
from .views.registration_views import Registrations, RegistrationDetail
from .views.user_views import SignUp, SignIn, SignOut, ChangePassword

urlpatterns = [
  	# Restful routing
    path('mangos/', Mangos.as_view(), name='mangos'),
    path('mangos/<int:pk>/', MangoDetail.as_view(), name='mango_detail'),
    path('courses/', Courses.as_view(), name='courses'),
    path('courses/<int:pk>/', CourseDetail.as_view(), name='course_detail'),
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('sign-out/', SignOut.as_view(), name='sign-out'),
    path('change-pw/', ChangePassword.as_view(), name='change-pw'),
    path('registrations/', Registrations.as_view(), name='registration'),
    path('registrations/', RegistrationDetail.as_view(), name='registration_detail')
]
