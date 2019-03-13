from rest_framework import serializers

from .models import Number

class RomanSerializer(serializers.Serializer):
   roman_number = serializers.CharField()

   def create(self, validated_data):
      return Number(**validated_data)

class IntSerializer(serializers.Serializer):
   int_number = serializers.IntegerField()

   def create(self, validated_data):
      return Number(**validated_data)