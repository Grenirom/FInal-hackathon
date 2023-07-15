from django.db import models

from account.models import CustomUser
from category.models import Category


# Create your models here.
class Comics(models.Model):
    STATUS = (
        ('in_stock', 'В наличии'),
        ('Out_of_stock', 'Нет в наличии'),
    )
    name = models.CharField(max_length=50, unique=True)
    published_at = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    price = models.DecimalField(max_digits=22, decimal_places=2)
    amount_of_pages = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.RESTRICT, related_name="comics")
    amount = models.PositiveIntegerField(default=10)

    def __str__(self):
        return self.name
