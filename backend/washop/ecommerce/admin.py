from .models import *
from django.contrib import admin
from django.apps import apps

'''
@admin.register(Negocio)
class NegocioAdmin(admin.ModelAdmin):
    list_display = ('nombre_negocio', 'direccion', 'whatsapp', 'rubro')
    list_filter = ('rubro', 'whatsapp')
    search_fields = ('nombre_negocio', 'rubro')'''





# Excluir modelos predefinidos de Django y TokenProxy de authtoken
excluded_models = ['Group', 'User', 'TokenProxy']

# Obtener todos los modelos de la aplicación actual
models_to_register = apps.get_models()

# Registrar todos los modelos en el administrador, excepto los excluidos
for model in models_to_register:
    if model.__name__ not in excluded_models:
        admin.site.register(model)
