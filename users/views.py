from django.shortcuts import render
from rest_framework import generics, authentication, permissions
from .models import Role, User
from rest_framework.response import Response
from .serializer import RoleSerializer, UserSerializer


# Create your views here.

#CRUD Role

class RoleListCreate(generics.ListCreateAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class RoleUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer



#CRUD User

class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication] #autenticacion de los tokens, seguridad
    permission_classes = [permissions.IsAuthenticated]


class UserUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer 
