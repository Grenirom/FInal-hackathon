from rest_framework import serializers
from .models import New


class NewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = New
        fields = ('id', 'image', 'category', 'title')


class NewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = New
        fields = '__all__'
