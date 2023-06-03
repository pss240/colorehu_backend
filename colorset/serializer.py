from rest_framework import serializers
from .models import ColorSet

class ColorSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = ColorSet
        fields = (
            'id',
            'uid',
            'color1',
            'color2',
            'color3',
            'color4',
            'color5',
            'colorsetstr',
            'share',
            'keyword',
            )