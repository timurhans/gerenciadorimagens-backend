from media.serializers import MediaSerializer
from rest_framework import serializers
from .models import Book

class BookViewSerializer(serializers.ModelSerializer):
    media = MediaSerializer(many=True)

    class Meta:
        model = Book
        fields = ('id', 'name', 'description', 'media')

class BookSerializer(serializers.ModelSerializer):
    # media = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ('id', 'name', 'description', 'media')
    
    # def validate(self, value):
    #     return value

    # def create(self, validated_data):
    #     print("a", validated_data)
    #     return super().create(validated_data)
    
    # def get_media(self, obj):
    #     print("obj ->>>>>", obj.data)
    #     request = self.context.get('request')
    #     query = Book.objects.get(name=request.data["name"])
    #     return [MediaSerializer(p).data for p in query.media]