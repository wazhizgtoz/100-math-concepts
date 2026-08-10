from django.contrib import admin
from .models import Modulo, Conceito

@admin.register(Modulo)
class ModuloAdmin(admin.ModelAdmin):
    list_display = ['nome', 'descricao', 'ordem']
    list_editable = ['ordem']
    search_fields = ['nome', 'descricao']

@admin.register(Conceito)
class ConceitoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'modulo', 'ordem', 'slug']
    list_filter = ['modulo']
    search_fields = ['titulo', 'explicacao']
    list_editable = ['ordem']
    prepopulated_fields = {'slug': ('titulo',)}
    # REMOVA estas linhas:
    # readonly_fields = ['created_at', 'updated_at']