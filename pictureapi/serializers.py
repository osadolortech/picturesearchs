from rest_framework import serializers
from .models import PictureModel

class PictureSerializer(serializers.ModelSerializer):
    image =serializers.ImageField(required=True)

    class Meta:
        model=PictureModel
        fields = ['id','title','image','uploaded_date']