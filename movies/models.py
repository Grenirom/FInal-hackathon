from random import randint
from django.db import models
from category.models import Category


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    release_date = models.DateField()
    director = models.CharField(max_length=100)
    actors = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.RESTRICT,
                                 related_name='movies')
    preview = models.ImageField(upload_to='images/', null=True)
    trailer = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ('created_at',)


class MovieImage(models.Model):
    title = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='images/')
    movie = models.ForeignKey(Movie, related_name='images', on_delete=models.CASCADE)

    def generate_name(self):
        return 'image' + str(randint(100000, 999999))

    def save(self, *args, **kwargs):
        self.title = self.generate_name()
        return super(MovieImage, self).save(*args, **kwargs)
