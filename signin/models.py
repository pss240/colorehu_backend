from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Signin(models.Model):
    id = models.AutoField(primary_key=True)
    nickname = models.CharField(max_length=200,)
    email = models.CharField(max_length=200)
