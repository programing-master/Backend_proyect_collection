# serializers.py
from rest_framework import serializers
from .models import CountriesModel

class CountriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CountriesModel
        fields = '__all__'