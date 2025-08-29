# fofocas/admin.py

from django.contrib import admin
from .models import Fofoca, Comentario

# Registra o modelo Fofoca
@admin.register(Fofoca)
class FofocaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_publicacao', 'tags')
    list_filter = ('tags', 'data_publicacao')
    search_fields = ('titulo', 'corpo')

# Registra o modelo Comentario
@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('fofoca', 'data_comentario', 'parent_comment')
    list_filter = ('fofoca', 'data_comentario')
    search_fields = ('corpo',)