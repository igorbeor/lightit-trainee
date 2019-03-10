from rest_framework import generics, permissions

from .serializers import NumberConverterSerializer
from .models import NumberConverter

class NumberCreate(generics.CreateAPIView):
    model = NumberConverter
    serializer_class = NumberConverterSerializer
    permission_classes = [
        permissions.AllowAny
    ]