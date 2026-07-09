from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'edificios', views.EdificioViewSet)
router.register(r'departamentos', views.DepartamentoViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('edificios_view/', views.listar_edificios, name='listar_edificios'),
    path('departamentos_view/', views.listar_departamentos, name='listar_departamentos'),
    path('api/', include(router.urls)),
]
