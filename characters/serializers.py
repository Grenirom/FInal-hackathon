from rest_framework import serializers
from .models import Character


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = '__all__'


class CharacterListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ('avatar', 'name')


