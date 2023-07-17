from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class ParsingModel(models.Model):
    name = models.CharField(max_length=1000)
    description = models.TextField()

    def __str__(self):
        return self.name


@receiver(post_save, sender=ParsingModel)
def slug_save(sender, instance, *args, **kwargs):
    print("Объект сохранен!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1")
