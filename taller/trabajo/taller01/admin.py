from django.contrib import admin
from .models import Edificio, Departamento

class EdificioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ciudad', 'tipo')
    list_filter = ('ciudad', 'tipo')
    search_fields = ('nombre', 'direccion')
    ordering = ('ciudad', 'nombre')

class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('nombre_propietario', 'costo', 'num_cuartos', 'edificio')
    list_filter = ('edificio', 'num_cuartos')
    search_fields = ('nombre_propietario', 'edificio__nombre')
    ordering = ('costo',)


admin.site.register(Edificio, EdificioAdmin)
admin.site.register(Departamento, DepartamentoAdmin)