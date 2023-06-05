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
        self.fields['uid'] = SigninSerializer(read_only=True).data['id']
        return super(ColorSetSerializer,self).to_representation(instance)

