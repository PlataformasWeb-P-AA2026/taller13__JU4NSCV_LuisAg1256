from django.db import models

class Edificio(models.Model):
    TIPO_CHOICES = [
        ('residencial', 'Residencial'),
        ('comercial', 'Comercial'),
    ]
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=150)
    ciudad = models.CharField(max_length=100)
    tipo = models.CharField(max_length=30, choices=TIPO_CHOICES)

    def __str__(self):
        return f"{self.nombre} ({self.ciudad} - {self.get_tipo_display()})"


class Departamento(models.Model):
    nombre_propietario = models.CharField(max_length=150, verbose_name="Nombre completo del propietario")
    costo = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Costo del departamento")
    num_cuartos = models.IntegerField(verbose_name="Número de cuartos")
    edificio = models.ForeignKey(Edificio, on_delete=models.CASCADE, related_name="departamentos")

    def __str__(self):
        return f"Propietario: {self.nombre_propietario} - Costo: {self.costo} - Cuartos: {self.num_cuartos}"
