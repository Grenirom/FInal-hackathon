from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from news.models import New

User = get_user_model()


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    new = models.ForeignKey(New, on_delete=models.CASCADE, related_name='likes')
    like = models.BooleanField(default=False)


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorite')
    new = models
