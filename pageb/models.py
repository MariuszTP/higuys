from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.


class Kategoria(models.Model):
    name = models.CharField(null=True, max_length=50)

    def __str__(self):
        return self.name

class Opinion(models.Model):
    name = models.CharField(null=True, max_length=2000)
    approval = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Gallery1(models.Model):
    kategoria = models.ForeignKey(Kategoria, on_delete=models.CASCADE, null=True)
    name = models.CharField(null=True, max_length=50)
    description = models.TextField(max_length=600, null=True, blank=False)
    image = models.ImageField(null=True)

    def __str__(self):
        return self.name

class Image3(models.Model):
    image = models.ImageField(null=True)
    default = models.BooleanField(default=False)


from django_google_maps import fields as map_fields

