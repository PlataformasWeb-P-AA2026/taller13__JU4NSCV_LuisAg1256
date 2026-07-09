from rest_framework import serializers
from .models import Edificio, Departamento

class EdificioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Edificio
        fields = ['url', 'nombre', 'direccion', 'ciudad', 'tipo']

class DepartamentoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Departamento
        fields = ['url', 'nombre_propietario', 'costo', 'num_cuartos', 'edificio']
