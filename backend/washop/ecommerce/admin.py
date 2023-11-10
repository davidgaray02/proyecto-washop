from django.contrib import admin
from .models import *   

'''
@admin.register(Negocio)
class NegocioAdmin(admin.ModelAdmin):
    list_display = ('nombre_negocio', 'direccion', 'whatsapp', 'rubro')
    list_filter = ('rubro', 'whatsapp')
    search_fields = ('nombre_negocio', 'rubro')'''


from django.apps import apps

# Obtener todos los modelos de la aplicación actual
models_to_register = apps.get_models()

# Excluir modelos predefinidos de Django
excluded_models = ['Group', 'User']  # Agrega los nombres de los modelos que deseas excluir

# Registrar todos los modelos en el administrador, excepto los excluidos
for model in models_to_register:
    if model.__name__ not in excluded_models:
        admin.site.register(model)


