from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from .serializers import MediaTypeSerializer, MediaStyleSerializer
from .serializers import ProductCollectionSerializer, ProductCategorySerializer, ProductSubCategorySerializer
from .models import MediaType, MediaStyle, ProductCategory, ProductCollection, ProductSubCategory
from rest_framework import status
from rest_framework.response import Response

class ViewMediaTypes(generics.ListAPIView):
    queryset = MediaType.objects.all()
    serializer_class = MediaTypeSerializer

class ViewMediaType(generics.RetrieveDestroyAPIView):
    queryset = MediaType.objects.all()
    serializer_class = MediaTypeSerializer

class CreateMediaType(generics.CreateAPIView):
    queryset = MediaType.objects.all()
    serializer_class = MediaTypeSerializer
    permission_classes = (IsAdminUser, )

class ViewMediaStyles(generics.ListAPIView):
    queryset = MediaStyle.objects.all()
    serializer_class = MediaStyleSerializer

class ViewMediaStyle(generics.RetrieveDestroyAPIView):
    queryset = MediaStyle.objects.all()
    serializer_class = MediaStyleSerializer

class CreateMediaStyle(generics.CreateAPIView):
    queryset = MediaStyle.objects.all()
    serializer_class = MediaStyleSerializer
    permission_classes = (IsAdminUser, )

class ViewProductCollections(generics.ListAPIView):
    queryset = ProductCollection.objects.all()
    serializer_class = ProductCollectionSerializer

class ViewProductCollection(generics.RetrieveDestroyAPIView):
    queryset = ProductCollection.objects.all()
    serializer_class = ProductCollectionSerializer

class CreateProductCollection(generics.CreateAPIView):
    queryset = ProductCollection.objects.all()
    serializer_class = ProductCollectionSerializer
    permission_classes = (IsAdminUser, )

class ViewProductCategories(generics.ListAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer

class ViewProductCategory(generics.RetrieveDestroyAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer

class CreateProductCategory(generics.CreateAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
    permission_classes = (IsAdminUser, )

class ViewProductSubCategories(generics.ListAPIView):
    queryset = ProductSubCategory.objects.all()
    serializer_class = ProductSubCategorySerializer

class ViewProductSubCategory(generics.RetrieveDestroyAPIView):
    queryset = ProductSubCategory.objects.all()
    serializer_class = ProductSubCategorySerializer

class CreateProductSubCategory(generics.CreateAPIView):
    queryset = ProductSubCategory.objects.all()
    serializer_class = ProductSubCategorySerializer
    permission_classes = (IsAdminUser, )
    