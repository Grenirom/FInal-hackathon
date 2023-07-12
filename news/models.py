from django.db import models
from category.models import Category


class New(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    published = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255, unique=True)
    image = models.ImageField(upload_to='news_img', blank=True, default='news_img/new_default.png')
    body = models.TextField(unique=True)

    def __str__(self):
        return self.title

