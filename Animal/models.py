import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Animal(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='animals')
    name = models.CharField(max_length=100, null=False)
    animal = models.CharField(max_length=100)
    race = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    birthdate = models.DateField(default=datetime.date.today)
    photo = models.ImageField(null=True,blank=True,default='',upload_to='imgAnimal/')