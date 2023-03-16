from dataclasses import fields
from rest_framework import routers, serializers, viewsets

# importacion de modelos
from Animal.models import Animal 

class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = ('__all__')