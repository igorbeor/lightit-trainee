from rest_framework import serializers

from .models import NumberConverter

class NumberConverterSerializer(serializers.ModelSerializer):
    class Meta:
        model = NumberConverter
        fields = ('id', 'roman_number', 'int_number')