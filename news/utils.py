from rest_framework import serializers
from .models import Like, Favorite, Rate, Comment
from . import serializers
from .serializers import FavoriteSerializer, ReviewerSerializer, FanSerializer


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


def delete_comment(obj, user):
    try:
        Comment.objects.get(new=obj, user=user).delete()
    except Comment.DoesNotExist:
        return 'No comment to delete!'


def is_commented(obj, user):
    try:
        return Comment.objects.filter(user=user, new=obj).exists()
    except TypeError:
        return False


def get_commenters(obj):
    commenters = Comment.objects.filter(new=obj)
    serializer = serializers.CommentSerializer(commenters, many=True)
    commenters = [{'user': i['user'], 'comment': i['comment']} for i in serializer.data]
    return commenters


def get_user_comments(user):
    comments = Comment.objects.filter(user=user)
    serializer = serializers.CommentSerializer(comments, many=True)
    comments = [{'new': i['new'], 'comment': i['comment']} for i in serializer.data]
    return comments


# RATING


def add_rating(user, obj, rating):
    if 0<= int(rating) <= 5:
        rating_obj, is_created = Rate.objects.get_or_create(user=user, new=obj)
        rating_obj.rating = rating
        rating_obj.save()
        if not is_created:
            return 'Updated rating'
        return 'Added rating'
    raise serializers.ValidationError('Entered an incorrect Rating!')


def delete_rating(user, obj):
    try:
        Rate.objects.filter(new=obj, user=user).delete()
    except Rate.DoesNotExist:
        return 'No rating to delete!'


def is_rater(obj, user):
    try:
        return Rate.objects.filter(user=user, new=obj).exists()
    except TypeError:
        return 'Rate Does Not Exist'


def get_rates(obj):
    users = Rate.objects.filter(new=obj)
    serializer = ReviewerSerializer(users, many=True)
    return serializer.data

# FAVORITES

def add_or_delete_favorite(user, obj):
    fav_obj, is_created = Favorite.objects.get_or_create(new=obj, user=user)
    fav_obj.is_favorite = not fav_obj.is_favorite
    fav_obj.save()
    if fav_obj.is_favorite:
        return 'Added to favorites'
    return 'Deleted from favorites'


def is_favorite(obj, user):
    try:
        return Favorite.objects.filter(user=user, new=obj, is_favorite=True).exists()
    except TypeError:
        return False

def get_favorites(user):
    try:
        new = Favorite.objects.filter(user=user, is_favorite=True)
        serializer = FavoriteSerializer(new, many=True)
        return serializer.data
    except TypeError:
        return []
