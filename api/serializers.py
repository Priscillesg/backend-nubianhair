from django.db.models.base import Model
from rest_framework import serializers
from .models import Favoris
from django.contrib.auth.models import User
from rest_framework.authtoken.views import Token

class FavorisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favoris
        fields = "__all__"
    # def create(self, validated_data):
    #     favoris = Favoris.objects.create(**validated_data)
    #     return favoris
    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.image_url = validated_data.get('image_url', instance.image_url)
    #     instance.business_id = validated_data.get('business_id ', instance.business_id )
    #     return instance
    # def display(self):
    #     favoris = Favoris.objects.all()
    #     return favoris


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']

        extra_kwargs = {'password':{
            'write_only':True,
            'required':True
        }}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user

