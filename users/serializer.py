from rest_framework import serializers
from .models import Role,User

class RoleSerializer(serializers.ModelSerializer): #esta heredando del modelo
    class Meta: 
        model = Role
        fields = '__all__' 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'  
