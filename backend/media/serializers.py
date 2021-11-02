from properties.serializers import MediaStyleSerializer, MediaTypeSerializer
from properties.models import MediaType
from tags.serializers import TagSerializer
from rest_framework import serializers
from .models import Media
from tags.models import Tag

class MediaViewSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    media_type = MediaTypeSerializer()
    style = MediaStyleSerializer()

    class Meta:
        model = Media
        fields = ('id', 'image', 'media_type', 'style', 'tags', 'is_private')

class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = ('id', 'image', 'media_type', 'style', 'tags', 'is_private')