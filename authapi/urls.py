
from django.contrib import admin
from django.urls import path
from authapi.views import SendPasswordRestEmailView, UserChangePasswordView, UserLoginView, UserPasswordResetView, UserProfileView, UserRegistrationView
# from django.conf.urls.static import static
# from django.conf import settings

# +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns = [

    path('register/', UserRegistrationView.as_view(),name='register'),
    path('login/', UserLoginView.as_view(),name='login'),
    path('profile/', UserProfileView.as_view(),name='profile'),
    path('changepassword/',UserChangePasswordView.as_view(),name='changepassword'),
    path('sendresetpasswordemail/',SendPasswordRestEmailView.as_view(),name='sendresetpasswordemail'),
    path('reset-password/<uid>/<token>/',UserPasswordResetView.as_view(),name='rest-password'),

]

