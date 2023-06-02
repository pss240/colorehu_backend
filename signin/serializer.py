from rest_framework import serializers
from .models import Signin

class SigninSerializer(serializers.ModelSerializer):
    class Meta:
        model = Signin
        fields = ('id','nickname','email',)