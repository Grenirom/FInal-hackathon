from django.db import models
from category.models import Category


class Character(models.Model):
    name = models.CharField(max_length=150, unique=True)
    avatar = models.ImageField(upload_to='character_images', blank=True, default='character_images/default-character'
                                                                                 '-img.jpg')
    short_description = models.CharField(max_length=255)
    biography = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
