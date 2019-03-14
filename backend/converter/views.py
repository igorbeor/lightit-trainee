from .models import NumberConverter
from django.http import Http404

# from .serializers import RomanSerializer, IntSerializer
from .serializers import NumberConverterSerializer
from .converter import Converter
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class RomanToIntView(APIView):

    def post(self, request, format=None):
        # c = Converter()
        # serializer = IntSerializer(data={"int_number":c.roman_to_int(request.data["roman_number"])})
        serializer = NumberConverterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class IntToRomanView(APIView):

    def post(self, request, format=None):
        # c = Converter()
        # serializer = RomanSerializer(data={"roman_number":c.int_to_roman(request.data["int_number"])})
        serializer = NumberConverterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)