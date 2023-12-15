from rest_framework import serializers
from .models import Pet
from django_filters import rest_framework as filters


class PetFilter(filters.FilterSet):
    class Meta:
        model = Pet
        fields = {
            "name": ["icontains"],
            "animal_type": ["exact"],
            "owner": ["icontains"]
            }

class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = "__all__"
        filter_class = PetFilter
