# UFVJM_Segredos_Project/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # A linha abaixo é a mais importante para o seu link funcionar
    path('', include('fofocas.urls')),
]