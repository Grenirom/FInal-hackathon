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


class FavoriteSerializer(serializers.Serializer):
    new = serializers.CharField()


class CommentSerializer(serializers.Serializer):
    user = serializers.EmailField()
    comment = serializers.CharField()
    new = serializers.CharField()


# class LikeSerializer(serializers.Serializer):
#     user