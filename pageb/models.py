from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(null=True, max_length=50)

    def __str__(self):
        return self.name

class Opinion(models.Model):
    text = models.CharField(null=True, max_length=2000)
    approval = models.BooleanField(default=False)

    def __str__(self):
        return self.text


class Gallery(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    name = models.CharField(null=True, max_length=50)
    image = models.ImageField(null=True)

    def __str__(self):
        return self.name





