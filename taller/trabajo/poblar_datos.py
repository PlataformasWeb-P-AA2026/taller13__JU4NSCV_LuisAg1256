import os
import django
from decimal import Decimal

# Configurar el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'trabajo.settings')
django.setup()

from taller01.models import Edificio, Departamento

def poblar():
    # Limpiar datos existentes
    print("Limpiando base de datos...")
    Departamento.objects.all().delete()
    Edificio.objects.all().delete()

    print("Creando edificios...")
    # Crear Edificios
    e1 = Edificio.objects.create(
        nombre="Edificio Torres del Sol",
        direccion="Av. 10 de Agosto y Orellana",
        ciudad="Quito",
        tipo="residencial"
    )
    e2 = Edificio.objects.create(
        nombre="Edificio Corporativo El Parque",
        direccion="Av. De los Shyris y Naciones Unidas",
        ciudad="Quito",
        tipo="comercial"
    )
    e3 = Edificio.objects.create(
        nombre="Torre Centenario",
        direccion="Malecón 2000 y 9 de Octubre",
        ciudad="Guayaquil",
        tipo="comercial"
    )
    e4 = Edificio.objects.create(
        nombre="Condominio La Loma",
        direccion="San Sebastián, Calle Larga",
        ciudad="Cuenca",
        tipo="residencial"
    )

    print("Creando departamentos...")
    # Crear Departamentos
    Departamento.objects.create(
        nombre_propietario="Juan Carlos Silva",
        costo=Decimal("120000.50"),
        num_cuartos=3,
        edificio=e1
    )
    Departamento.objects.create(
        nombre_propietario="María Augusta López",
        costo=Decimal("95000.00"),
        num_cuartos=2,
        edificio=e1
    )
    Departamento.objects.create(
        nombre_propietario="Luis Alejandro Gómez",
        costo=Decimal("250000.00"),
        num_cuartos=4,
        edificio=e4
    )
    Departamento.objects.create(
        nombre_propietario="Ana Lucía Ramírez",
        costo=Decimal("450000.00"),
        num_cuartos=10,
        edificio=e2
    )
    Departamento.objects.create(
        nombre_propietario="Carlos Alberto Mendoza",
        costo=Decimal("380000.00"),
        num_cuartos=8,
        edificio=e3
    )

    print(f"Población exitosa. Edificios creados: {Edificio.objects.count()}, Departamentos creados: {Departamento.objects.count()}.")

if __name__ == '__main__':
    poblar()
