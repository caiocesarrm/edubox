from rest_framework import serializers
from edubox.users.models import User

class CreateAuthUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=200)
    confirm_password = serializers.CharField(max_length=200)

    class Meta:
        model = User
        fields = (['id',
                   'email',
                   'name',
                   'password',
                   'confirm_password'])

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (['id',
                   'email',
                   'name',])
    
    def create(self, validated_data):
        return User.objects.create(**validated_data)
