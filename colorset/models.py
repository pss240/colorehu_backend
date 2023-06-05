from django.db import models

from colorehu import settings

# Create your models here.

class ColorSet(models.Model):
    id = models.AutoField(primary_key=True)
    uid = models.ForeignKey('signin.Signin',on_delete=models.CASCADE,db_column='uid')
    color1 = models.CharField(max_length=200,null=False)
    color2 = models.CharField(max_length=200,null=True,default='')
    color3 = models.CharField(max_length=200,null=True,default='')
    color4 = models.CharField(max_length=200,null=True,default='')
    color5 = models.CharField(max_length=200,null=True,default='')
    colorsetstr = models.CharField(max_length=200, default="none")
    share = models.BooleanField(default=False)
    keyword = models.CharField(max_length=200)