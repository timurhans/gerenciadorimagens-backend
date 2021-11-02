from rest_framework import serializers
from .models import NewUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields = ('email', 'first_name', 'surname', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = NewUser.objects.create_user(**validated_data)
        return user

class UserAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields = ('email', 'first_name', 'surname', 'password', 'is_staff')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = NewUser.objects.create_user(**validated_data)
        return user