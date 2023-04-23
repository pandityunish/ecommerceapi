from django.forms import ValidationError
from rest_framework import serializers
from authapi.models import User
from django.utils.encoding import smart_str,force_bytes,DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.contrib.auth.tokens import PasswordResetTokenGenerator


class UserRegistrationViewSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'phone_number','tc','password2', 'name']
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        if password != password2:
            raise serializers.ValidationError("Password and Confirm Password doesn't match")
        return attrs
    
    def create(self, validated_data):
      return User.objects.create_user(**validated_data)


class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(
        label="Password",
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    class Meta:
        model = User
        fields = ('email', 'password')

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = User.objects.filter(email=email).first()
            if user:
                if not user.check_password(password):
                    raise serializers.ValidationError('Invalid Password')
            else:
                raise serializers.ValidationError('Invalid Email')
        else:
            raise serializers.ValidationError('Email and Password are required')

        attrs['user'] = user
        return attrs



class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','email','name']


class UserChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=255, style={'input_type': 'password'}, write_only=True)
    class Meta:
        model = User
        fields = ['password']

    def validate(self, attrs):
        user = self.context.get('user')
        password = attrs.get('password')
        if not user.check_password(password):
            raise serializers.ValidationError("Current password is incorrect")
        return attrs

    def create(self, validated_data):
        user = self.context.get('user')
        password = validated_data.get('password')
        user.set_password(password)
        user.save()
        return user
    

class SendPasswordResetEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)

    class Meta:
        fields = ['email']

    def validate(self, attrs):
        email = attrs.get('email')
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = PasswordResetTokenGenerator().make_token(user)
            link = "http://localhost:3000/api/reset/" + uid + '/' + token
            print("password reset link", link)
            #Send Email
            body='Click following link to reset you password'+link
            data={
                'subject':'reset you password',
                'body':body,
                'to_email':user.email

            }
            return attrs
        else:
            raise serializers.ValidationError("You are not a registered user.")
        


# class UserPasswordResetSerializer(serializers.Serializer):
#     password = serializers.CharField(max_length=255, style={'input_type': 'password'}, write_only=True)

#     class Meta:
#         model = User
#         fields = ['password']

#     def validate(self, attrs):
#         user = self.context.get('user')
#         uid = self.context.get('uid')
#         token = self.context.get('token')
#         password = attrs.get('password')

#         if not user.check_password(password):
#             raise serializers.ValidationError("Current password is incorrect")

#         id = smart_str(urlsafe_base64_decode(uid))
#         user = User.objects.get(id=id)

#         if not PasswordResetTokenGenerator().check_token(user, token):
#             raise ValidationError('Token is not valid or expired')

#         return attrs

#     def create(self, validated_data):
#         user = self.context.get('user')
#         password = validated_data.get('password')
#         user.set_password(password)
#         user.save()
#         return user



class UserPasswordResetSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=255, style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['password']

    def validate(self, attrs):
        user = self.context.get('user')
        if not user:
            raise serializers.ValidationError('Invalid user')
            
        uid = self.context.get('uid')
        token = self.context.get('token')
        password = attrs.get('password')

        if not user.check_password(password):
            raise serializers.ValidationError("Current password is incorrect")

        id = smart_str(urlsafe_base64_decode(uid))
        user = User.objects.get(id=id)

        if not PasswordResetTokenGenerator().check_token(user, token):
            raise ValidationError('Token is not valid or expired')

        return attrs

    def create(self, validated_data):
        user = self.context.get('user')
        password = validated_data.get('password')
        user.set_password(password)
        user.save()
        return user
