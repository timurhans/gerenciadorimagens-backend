from rest_framework import generics, status
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from .serializers import BookSerializer, BookViewSerializer
from .models import Book


class ViewBooks(generics.ListAPIView):
    serializer_class = BookViewSerializer
    queryset = Book.objects.order_by("-created_at")
    pagination_class = LimitOffsetPagination

class BookDetails(generics.RetrieveAPIView):
    serializer_class = BookViewSerializer
    queryset = Book.objects.all()

class AdminViewBooks(generics.ListCreateAPIView):
    serializer_class = BookViewSerializer
    queryset = Book.objects.order_by("-created_at")
    pagination_class = LimitOffsetPagination
    permission_classes = (IsAdminUser, )

    def post(self, request, format=None):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AdminBookDetails(generics.RetrieveDestroyAPIView):
    serializer_class = BookViewSerializer
    queryset = Book.objects.all()
    permission_classes = (IsAdminUser, )

    def get(self, request, pk):
        queryset = Book.objects.get(pk=pk)
        serializer = BookViewSerializer(queryset)
        return Response(serializer.data)

    def patch(self, request, pk):
        instance = Book.objects.get(pk=pk)
        serializer = BookSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        error = {
            "Error": "The provided data isn't valid"
        }
        return Response(error, status=status.HTTP_400_BAD_REQUEST)