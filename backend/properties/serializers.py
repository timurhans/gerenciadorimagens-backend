from rest_framework import serializers
from .models import MediaStyle, MediaType, ProductCategory, ProductSubCategory, ProductCollection

class MediaTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaType
        fields = ('id', 'name')

class MediaStyleSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaStyle
        fields = ('id', 'name')
        
class ProductCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCollection
        fields = ('id', 'name')

class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ('id', 'name')

class ProductSubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSubCategory
        fields = ('id', 'name')