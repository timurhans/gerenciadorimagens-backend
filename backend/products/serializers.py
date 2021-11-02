from properties.serializers import ProductCategorySerializer, ProductCollectionSerializer, ProductSubCategorySerializer
from rest_framework import serializers
from .models import ColorVariationForProducts, Product
from media.serializers import MediaSerializer

class ViewColorVariationSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField(source="product.id")

    class Meta:
        model = ColorVariationForProducts
        fields = ('id', 'product', 'color', 'media')
    
    def to_representation(self, instance):
        request = self.context.get('request')
        data = [MediaSerializer(m).data for m in instance.media.all()]
        for entry in data:
            entry["image"] = request.build_absolute_uri(entry["image"])
        return {
            'id': instance.id,
            'product': instance.product.name,
            'color': instance.color.name,
            'media': data
        }

class ColorVariationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ColorVariationForProducts
        fields = ('id', 'product', 'color', 'media')

class ProductViewSerializer(serializers.ModelSerializer):
    color_variations = serializers.SerializerMethodField()
    media = MediaSerializer(many=True)
    category = ProductCategorySerializer()
    subcategory = ProductSubCategorySerializer()
    collection = ProductCollectionSerializer()

    class Meta:
        model = Product
        fields = (
            'id', 'name',
            'media', 'color_variations', 'category',
            'collection', 'subcategory'
        )
    
    def get_color_variations(self, obj):
        request = self.context.get('request')
        query = ColorVariationForProducts.objects.filter(product=obj)
        return [ViewColorVariationSerializer(p, context={"request": request}).data for p in query]

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id', 'name',
            'media', 'color_variations', 'category',
            'collection', 'subcategory',
        )