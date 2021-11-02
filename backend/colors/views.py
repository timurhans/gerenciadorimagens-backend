from rest_framework import generics, status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from colors.serializers import ColorSerializer
from .models import Color

class ViewColors(generics.ListAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer

class CreateColor(generics.CreateAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
    permission_classes = (IsAdminUser, )

class AdminColorDetails(generics.RetrieveDestroyAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
    permission_classes = (IsAdminUser, )

    def patch(self, request, pk):
        instance = Color.objects.get(pk=pk)
        request.data['code'] = request.data['code'][1:]
        serializer = ColorSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        error = {
            "Error": "The provided data isn't valid"
        }
        return Response(error, status=status.HTTP_400_BAD_REQUEST)