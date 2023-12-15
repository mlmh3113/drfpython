from django.shortcuts import render
from rest_framework import viewsets
from .models import Pet
from .serializers import PetSerializer


class PetViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer

    def get_queryset(self):
        queryset = Pet.objects.all()
        name = self.request.query_params.get("name", None)
        animal_type = self.request.query_params.get("animal_type", None)
        owner = self.request.query_params.get("owner", None)
        if name is not None:
            queryset = queryset.filter(name__icontains=name)
            return queryset
        elif animal_type is not None:
            queryset = queryset.filter(animal_type__exact=animal_type)
            return queryset
        elif owner is not None:
            queryset = queryset.filter(owner__icontains=owner)
            return queryset
        else:
            return queryset
