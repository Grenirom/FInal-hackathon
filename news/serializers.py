from django.db.models import Avg
from rest_framework import serializers
from .models import New, Like, Rate, Comment
from . import utils


# class NewListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = New
#         fields = ('id', 'image', 'category', 'title')
#
#
# class NewCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = New
#         fields = '__all__'


class FavoriteSerializer(serializers.Serializer):
    new = serializers.CharField()


class CommentSerializer(serializers.Serializer):
    user = serializers.EmailField()
    comment = serializers.CharField()
    new = serializers.CharField()


class FanSerializer(serializers.Serializer):
    user = serializers.CharField(required=True)


class ReviewerSerializer(serializers.Serializer):
    user = serializers.CharField()
    rating = serializers.IntegerField()


class NewSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = New
        fields = '__all__'

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        user = self.context.get('request').user
        repr['likes'] = Like.objects.filter(new=instance, like=True).count()
        rating = Rate.objects.filter(new=instance).aggregate(Avg('rating'))['rating__avg']
        if rating:
            repr['rating'] = rating
        else:
            repr['rating'] = 0
        comments = Comment.objects.filter(new=instance)
        comments = CommentSerializer(comments, many=True).data
        comments = [{'user': i['user'], 'comment': i['comment']} for i in comments]
        repr['comments'] = comments
        repr['is_fan'] = utils.is_fan(user=user, obj=instance)
        repr['is_reviewer'] = utils.is_rater(user=user, obj=instance)
        repr['is_commented'] = utils.is_commented(user=user, obj=instance)
        repr['is_favorite'] = utils.is_favorite(user=user, obj=instance)
        return repr