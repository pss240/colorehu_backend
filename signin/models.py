from django.db import models

# Create your models here.


class Signin(models.Model):
    nickname = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
