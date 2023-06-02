from django.db import models

# Create your models here.


class Colorsetrecommend(models.Model):
    color1 = models.CharField(max_length=200,null=False)
    color2 = models.CharField(max_length=200,blank=True)
    color3 = models.CharField(max_length=200,blank=True)
    color4 = models.CharField(max_length=200,blank=True)
    color5 = models.CharField(max_length=200,blank=True)
    colorsetstr = models.CharField(max_length=200)
    share = models.BooleanField(default=False)
    keyword = models.CharField(max_length=200)