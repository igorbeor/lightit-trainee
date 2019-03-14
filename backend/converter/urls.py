from django.urls import include, path

from .views import RomanToIntView, IntToRomanView

urlpatterns = [
    path('roman_to_int/', RomanToIntView.as_view()),
    path('int_to_roman/', IntToRomanView.as_view()),
]