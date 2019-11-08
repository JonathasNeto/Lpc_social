from django.contrib import admin
from .models import Comentario,Publicao,Perfil

@admin.register(Comentario,Publicao,Perfil)
class rede_social(admin.ModelAdmin):
    pass
