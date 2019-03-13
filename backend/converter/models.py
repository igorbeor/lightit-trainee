from django.db import models

class Number:
    def __init__(self, **entries):
        self.__dict__.update(entries)