from .models import NumberConverter
from django.http import Http404

from .serializers import NumberConverterSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class Number(APIView):
    def get_object(self, pk):
        try:
            return NumberConverter.objects.get(pk=pk)
        except NumberConverter.DoesNotExist:
            raise Http404


    def get(self, request, pk):
        number = self.get_object(pk)
        number = NumberConverterSerializer(number)
        return Response(number.data)
