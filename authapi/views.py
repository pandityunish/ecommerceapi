from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from authapi.serializers import SendPasswordResetEmailSerializer, UserPasswordResetSerializer, UserProfileSerializer, UserRegistrationViewSerializer,UserChangePasswordSerializer
from django.contrib.auth import authenticate
from authapi.renders import UserRender
from authapi.serializers import UserLoginSerializer 
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

#Generate Token Mannually
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

#User Registration 
class UserRegistrationView(APIView):
    renderer_classes=[UserRender]
    permission_classes = (AllowAny,)  # Allow any user to access this view
    
    def post(self, request, format=None):
        serializer=UserRegistrationViewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user=serializer.save()
            token= get_tokens_for_user(user)
            return Response({'token':token,'msg': 'Registration Successful'},
                            status=status.HTTP_201_CREATED)

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

#User Login
class UserLoginView(APIView):
    permission_classes = (AllowAny,) 
     # Allow any user to access this view
    def post(self,request,format=None):

        serializer=UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email=serializer.data.get("email")
            password= serializer.data.get("password")
            user=authenticate(email=email,password=password)
            if user is not None:
                token= get_tokens_for_user(user)
                return Response({'token':token,'msg':'Login Success'},status=status.HTTP_200_OK)
            else:
                return Response({'Errors':{'non_field_errors':['Email or Password is not valid']}},status=status.HTTP_404_NOT_FOUND)

     
# User Profile
class UserProfileView(APIView):
       renderer_classes=[UserRender]
       permission_classes = [IsAuthenticated]
       def get(self,request,format=None):
           serializer= UserProfileSerializer(request.user)
           return Response(serializer.data,status=status.HTTP_200_OK)
       

# User Change Password
class UserChangePasswordView(APIView):
    renderer_classes = [UserRender]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = UserChangePasswordSerializer(data=request.data, context={'user': request.user})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'msg': 'Password Change Successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# User PasswordResetEmail
class SendPasswordRestEmailView(APIView):
    renderer_classes = [UserRender]
    permission_classes = [IsAuthenticated]

    def post(self,request,format=None):
       serializer= SendPasswordResetEmailSerializer(data=request.data)
       if serializer.is_valid(raise_exception=True):
           return Response({'msg':'Password Reset link send. Please Check Your Email'},status=status.HTTP_200_OK)
           
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# User PasswordResetView
class UserPasswordResetView(APIView):
    renderer_classes = [UserRender]
    permission_classes = [AllowAny]

    def post(self,request,uid,token,format=None):
       serializer= UserPasswordResetSerializer(data=request.data,context={'uid':uid,'token':token})
       if serializer.is_valid(raise_exception=True):
           return Response({'msg':'Password Reset Successfully'},status=status.HTTP_200_OK)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
           



           