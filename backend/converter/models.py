from django.db import models

from .converter import Converter

class NumberConverter(models.Model):
    roman_number = models.CharField(max_length=255)
    int_number = models.IntegerField()

    def save(self, *args, **kwargs):
        converter = Converter()
        if not self.roman_number:
            self.int_number = converter.roman_to_int(self.roman_number)
        else:
            self.roman_number = converter.int_to_roman(self.int_number)
        super(NumberConverter, self).save(*args, **kwargs)