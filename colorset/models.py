from django.db import models

from colorehu import settings

# Create your models here.


class ColorSet(models.Model):
    uid = models.ForeignKey('signin.Signin',on_delete=models.CASCADE,db_column='uid')
    color1 = models.CharField(max_length=200,null=False)
    color2 = models.CharField(max_length=200,blank=True)
    color3 = models.CharField(max_length=200,blank=True)
    color4 = models.CharField(max_length=200,blank=True)
    color5 = models.CharField(max_length=200,blank=True)
    colorsetstr = models.CharField(max_length=200)
    share = models.BooleanField(default=False)
    keyword = models.CharField(max_length=200)