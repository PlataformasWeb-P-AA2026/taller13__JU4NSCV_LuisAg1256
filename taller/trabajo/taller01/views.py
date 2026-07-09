from django.shortcuts import render
from django.db.models import Sum
from .models import Edificio, Departamento

def index(request):
    total_edificios = Edificio.objects.count()
    total_departamentos = Departamento.objects.count()
    
    context = {
        'total_edificios': total_edificios,
        'total_departamentos': total_departamentos,
    }
    return render(request, 'index.html', context)

def listar_edificios(request):
    edificios = Edificio.objects.all()
    context = {
        'edificios': edificios
    }
    return render(request, 'listar_edificios.html', context)

def listar_departamentos(request):
    departamentos = Departamento.objects.all()
    context = {
        'departamentos': departamentos
    }
    return render(request, 'listar_departamentos.html', context)

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import EdificioSerializer, DepartamentoSerializer

class EdificioViewSet(viewsets.ModelViewSet):
    queryset = Edificio.objects.all()
    serializer_class = EdificioSerializer
    permission_classes = [IsAuthenticated]

class DepartamentoViewSet(viewsets.ModelViewSet):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer
    permission_classes = [IsAuthenticated]
