# fofocas/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_fofocas, name='lista_fofocas'),
    path('fofoca/<int:pk>/', views.detalhes_fofoca, name='detalhes_fofoca'),
    path('nova/', views.nova_fofoca, name='nova_fofoca'),
    path('reagir/', views.reagir_fofoca, name='reagir_fofoca'), # Adicione esta linha
]