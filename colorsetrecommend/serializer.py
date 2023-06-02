from rest_framework import serializers
from .models import Colorsetrecommend

class ColorsetrecommendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colorsetrecommend
        fields = (
            'color1',
            'color2',
            'color3',
            'color4',
            'color5',
            'keyword',
            
            )