from rest_framework import serializers
from .models import Drone
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import Serializer
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt

class DroneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drone
        fields = ['id', 'name', 'serial_number', 'status', 'battery_percentage', 'latitude', 'longitude']
    
# @csrf_exempt
class UserSerializer(serializers.ModelSerializer):
    permissions = serializers.SerializerMethodField()

    def get_permissions(self, obj):
        return list(obj.get_all_permissions())

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'permissions'
        ]
    # class Meta:
    #     model = User 
    #     fields = ('id', 'first_name', 'last_name', 'username', 'email', 'password')
    #     extra_kwargs = {
    #         'password' : {'write_only':True}
    #     }
    
    # def create(self,validated_data):
    #     user = User(
    #         username   = validated_data['username'],
    #         email      = validated_data['email'],
    #         first_name = validated_data['first_name'],
    #         last_name  = validated_data['last_name'] 
    #     )
    #     user.set_password(validated_data['password'])
    #     user.save()
    #     return user
    #     # password = validated_data.pop('password')
    #     # user = User.objects.create_user(password=password, **validated_data)
    #     # return user
    
    # def update(self, instance, validated_data):

    #     for attr, value in validated_data.items():

    #         if attr == 'password':
    #             instance.set_password(value)
    #         else:
    #             setattr(instance, attr, value)

    #     instance.save()
    #     return instance
    
    # def destroy(self, instance,validated_data):
    #     instance = self.get_object()
    #     instance.delete()

    #     return instance


class LoginSerializer(Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only = True)

    def validate(self, data):
        user = User.objects.filter(username = data['username']).first()
        if user and user.check_password(data['password']):
            return user
        raise ValidationError({'error': 'Invalid username or password'}) 

