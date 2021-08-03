from django.db.models.base import Model
from rest_framework import serializers
from .models import Favoris

class FavorisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favoris
        fields = "__all__"