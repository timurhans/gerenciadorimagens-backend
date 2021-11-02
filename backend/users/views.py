from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework import generics, serializers, status
from rest_framework.views import APIView
from django.contrib.auth import authenticate

from .serializers import UserAdminSerializer, UserSerializer
from .models import NewUser

import base64

class CreateUser(generics.CreateAPIView):
    queryset = NewUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny, )

class CreateUserByAdmin(generics.CreateAPIView):
    queryset = NewUser.objects.all()
    serializer_class = UserAdminSerializer
    permission_classes = (IsAdminUser, )

class ViewUsers(generics.ListAPIView):
    queryset = NewUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser, )

    def post(self, request, format=None):
        try:
            email = request.data['email']
            user = self.queryset.filter(email=email).values()[0]
            returnFields = {
                "email": email,
                "password": user["password"],
                "first_name": user["first_name"],
                "is_staff": user["is_staff"]
            }
            return Response(returnFields, status=status.HTTP_200_OK)
        except:
            error = {
                "Error": "The provided email isn't valid"
            }
            return Response(error, status=status.HTTP_400_BAD_REQUEST)

class UserLogin(APIView):
    queryset = NewUser.objects.all()
    serializer_class = UserSerializer

    def post(self, request, format=None):
        try:
            email = request.data['email']
            password = request.data['password']
            user = authenticate(email=email, password=password)


            returnFields = {
                "email": user.email,
                "first_name": user.first_name,
                "surname": user.surname,
                "is_staff": user.is_staff,
            }

            if user.is_staff:
                token = f'{email}:{password}'
                token = token.encode("ascii")
                token = base64.b64encode(token)
                returnFields["token"] = token
                
            return Response(returnFields, status=status.HTTP_200_OK)
        except:
            error = {
                "Error": "Invalid credentials"
            }
            return Response(error, status=status.HTTP_400_BAD_REQUEST)
