from django.db import models

from account.models import CustomUser
from category.models import Category


# Create your models here.
<<<<<<< HEAD
class   Comics(models.Model):
    STATUS_CHOISES = (
        ('in_stock', 'В наличии'),
        ('out_of_stock', 'Не в наличии'),
=======
class Comics(models.Model):
    STATUS = (
        ('in_stock', 'В наличии'),
        ('Out_of_stock', 'Нет в наличии'),
>>>>>>> e68ec5c748961dc1d2e14e698461137733ee98c5
    )
    name = models.CharField(max_length=50, unique=True)
    published_at = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    price = models.DecimalField(max_digits=22, decimal_places=2)
    amount_of_pages = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.RESTRICT, related_name="comics")
<<<<<<< HEAD
    stock = models.CharField(choices=STATUS_CHOISES, max_length=50)
=======
    amount = models.PositiveIntegerField(default=10)

>>>>>>> e68ec5c748961dc1d2e14e698461137733ee98c5
    def __str__(self):
        return self.name
