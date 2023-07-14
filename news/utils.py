from rest_framework import serializers
from .models import Like, Favorite, Rate, Comment
from . import serializers
# LIKE

def like_unlike(user, obj):
    like_obj, is_created = Like.objects.get_or_create(user=user, new=obj)
    like_obj.like = not like_obj.like
    like_obj.save()
    if not like_obj.like:
        return 'unliked'
    return 'liked'


def is_fan(user, obj):
    try:
        like = Like.objects.filter(user=user, new=obj)
        if like.exists() and like[0].like:
            return True
        return False
    except TypeError:
        return False


def get_fans(obj):
    fans = Like.objects.filter(new=obj, like=True)
    serializer = FanSerializer(fans, many=True)
    return serializer.data

# COMMENTS


def add_comment(user, obj, comment):
    comment_obj, is_created = Comment.objects.get_or_create(user=user, new=obj)
    comment_obj.comment = comment
    comment_obj.save()
    if is_created:
        return 'Added comment'
    return 'Updated comment'


def delete_comment(user, obj):
    try:
        Comment.objects.get(new=obj, user=user).delete()
    except Comment.DoesNotExist:
        return ValueError('No comment to delete!')


def is_commented(obj, user):
    try:
        return Comment.objects.filter(user=user, new=obj).exists()
    except TypeError:
        return False


def get_commenters(obj):
    commenters = Comment.objects.filter(new=obj)
    serializer = serializers.CommentSerializer(commenters, many=True)
    commenters = [{'user': i['user'], 'comment': i['comment']}]