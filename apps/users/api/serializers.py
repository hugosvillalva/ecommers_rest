from rest_framework import serializers
from apps.users.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UserlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = User


    def to_representation(self, instance):
        return {
            'id': instance['id'],
            'username': instance['username'],
            'email': instance['email'],
            'password': instance['password'],
            'name' : instance['name'],
            'last_name': instance['last_name']
        }
    
class PasswordSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=128, min_length=6, write_only=True)
    password2 = serializers.CharField(max_length=128, min_length=6, write_only=True)

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError(
                {'password':'Debe ingresar ambas contraseñas iguales'}
            )
        return data

class updateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email','name', 'last_name')
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'name','last_name')

class CustomObtainPairSerializer(TokenObtainPairSerializer):
    pass
