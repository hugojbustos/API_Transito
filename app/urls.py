from django.urls import path
from .views import CargarInfraccionView, ListarInfraccionesView

urlpatterns = [
    path('cargar_infraccion/', CargarInfraccionView.as_view(),
         name='cargar_infraccion'),
    path('listar_infracciones/', ListarInfraccionesView.as_view(),
         name='listar_infracciones'),
]
