from rest_framework import serializers

from signin.serializer import SigninSerializer
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
    def to_representation(self,instance):
        response = super().to_representation(instance)
        response['uid'] = SigninSerializer(instance.uid).data
        print(response['uid'])
        return response

