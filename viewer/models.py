from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=128, null=True, blank=True)
    year = models.PositiveIntegerField(default=2012, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    photo = models.ImageField(upload_to="movies/", null=True, blank=True)


# 1. Crearea unui model nou
# 2. Adaugarea a doua elemente
# 3. Actualizarea unui element
# 4. Stergerea unui element

class Actors(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    gender = models.CharField(max_length=20, null=True, blank=True)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
