from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from tags.serializers import TagSerializer
from rest_framework import generics, status
from .models import Tag


class ViewTags(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class TagDetails(generics.RetrieveAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class AdminViewTags(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (IsAdminUser, )

class AdminTagDetails(generics.RetrieveDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (IsAdminUser, )

    def patch(self, request, pk):
        instance = Tag.objects.get(pk=pk)
        serializer = TagSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        error = {
            "Error": "The provided data isn't valid"
        }
        return Response(error, status=status.HTTP_400_BAD_REQUEST)