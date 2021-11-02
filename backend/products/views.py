from products.filters import product_filter, public_product_filter
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAdminUser
from products.serializers import ColorVariationSerializer, ProductSerializer, ProductViewSerializer, ViewColorVariationSerializer
from products.models import ColorVariationForProducts, Product
from rest_framework import generics, status
from rest_framework.response import Response

class ViewProducts(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductViewSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        return public_product_filter(self)

class ProductDetails(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductViewSerializer

class AdminViewProducts(generics.ListCreateAPIView, LimitOffsetPagination):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = (IsAdminUser, )

    def get_queryset(self):
        return product_filter(self)

    def get(self, request):
        products = Product.objects.order_by("-created_at")
        queryset = self.paginate_queryset(products)
        serializer = ProductViewSerializer(queryset, many=True, context={"request": request})
        return self.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AdminProductDetails(generics.RetrieveDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductViewSerializer
    permission_classes = (IsAdminUser, )

    def patch(self, request, pk):
        instance = Product.objects.get(pk=pk)
        serializer = ProductSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        error = {
            "Error": "The provided data isn't valid"
        }
        return Response(error, status=status.HTTP_400_BAD_REQUEST)

class CreateColorVariation(generics.CreateAPIView):
    queryset = ColorVariationForProducts.objects.all()
    serializer_class = ColorVariationSerializer
    permission_classes = (IsAdminUser, )

class AdminGetColorVariations(generics.RetrieveUpdateDestroyAPIView):
    queryset = ColorVariationForProducts.objects.all()
    serializer_class = ColorVariationSerializer
    permission_classes = (IsAdminUser, )

    def get(self, request, pk):
        queryset = ColorVariationForProducts.objects.get(pk=pk)
        serializer = ViewColorVariationSerializer(queryset, context={"request": request})
        return Response(serializer.data)