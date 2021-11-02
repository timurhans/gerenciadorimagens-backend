from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from .serializers import MediaSerializer, MediaViewSerializer
from .models import Media
from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser, MultiPartParser
from rest_framework.pagination import LimitOffsetPagination

from rest_framework import status
from rest_framework.response import Response

from media.filters import media_filter


class ViewPublicMedia(generics.ListAPIView):
    queryset = Media.public_objects.all()
    serializer_class = MediaViewSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        return media_filter(self)

class PublicMediaDetail(generics.RetrieveAPIView):
    queryset = Media.public_objects.all()
    serializer_class = MediaViewSerializer

    def get_queryset(self):
        return media_filter(self)

class ViewMedia(generics.ListCreateAPIView):
    queryset = Media.objects.all()
    serializer_class = MediaViewSerializer
    pagination_class = LimitOffsetPagination
    parser_class = (FileUploadParser, MultiPartParser)
    permission_classes = (IsAdminUser, )

    def get_queryset(self):
        return media_filter(self)

    def post(self, request, format=None):
        serializer = MediaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MediaDetail(generics.RetrieveDestroyAPIView):
    queryset = Media.objects.all()
    serializer_class = MediaViewSerializer
    permission_classes = (IsAdminUser, )

    def patch(self, request, pk):
        instance = Media.objects.get(pk=pk)
        serializer = MediaSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        error = {
            "Error": "The provided data isn't valid"
        }
        return Response(error, status=status.HTTP_400_BAD_REQUEST)



