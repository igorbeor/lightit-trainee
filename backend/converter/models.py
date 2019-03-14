from django.db import models
from .converter import Converter

# class Number:
#     def __init__(self, **entries):
#         self.__dict__.update(entries)

class NumberConverter(models.Model):
    roman_number = models.CharField(max_length=25, blank=True)
    int_number = models.IntegerField()

    def save(self, *args, **kwargs):
        c = Converter()
        if not self.roman_number:
            self.roman_number = c.int_to_roman(self.int_number)
        else:
            self.int_number = c.roman_to_int(self.roman_number)
        super().save(*args, **kwargs)