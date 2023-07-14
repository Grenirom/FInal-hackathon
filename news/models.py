from django.contrib.auth import get_user_model
from django.db import models
from category.models import Category
from django.core.validators import MinValueValidator, MaxValueValidator

User = get_user_model()


class New(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    published = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255, unique=True)
    image = models.ImageField(upload_to='news_img', blank=True, default='news_img/new_default.png')
    body = models.TextField(unique=True)

    def __str__(self):
        return self.title


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    new = models.ForeignKey(New, on_delete=models.CASCADE, related_name='likes')
    like = models.BooleanField(default=False)


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
    new = models.ForeignKey(New, on_delete=models.CASCADE, related_name='favorites')
    is_favorite = models.BooleanField(default=False)


class Rate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rating')
    new = models.ForeignKey(New, on_delete=models.CASCADE, related_name='rating')
    rating = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(5),
        ], blank=True, null=True
    )


class Comment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    new = models.ForeignKey(New, on_delete=models.CASCADE, related_name='comments')

