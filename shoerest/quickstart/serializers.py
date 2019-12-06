from django.contrib.auth.models import User, Group
from shoerest.quickstart.models  import *
from  rest_framework import serializers

class ManufacturerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ['name', 'website']

class ShoeTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShoeType
        fields = ['style']

class ShoeColorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShoeColor
        fields = ['color_name']

class ShoeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Shoe
        fields = ['size', 'brand_name','manufacturer', 'color', 'material', 'shoe_type', 'fasten_type']