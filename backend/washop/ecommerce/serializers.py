from rest_framework import serializers
from django.contrib.auth.models import User
from . import models #Importar todos los modelos desde la raiz 

# MODULO USUARIOS

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Usuario  # O tu modelo de Usuario
        fields = '__all__'

# MODULO NEGOCIO

class RubroSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Rubro 
        fields = '__all__'

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Rol  
        fields = '__all__'

class NegocioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Negocio  
        fields = '__all__'

class UsuarioNegocioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UsuarioNegocio  
        fields = '__all__'


# MODULO INVENTARIO

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Categoria  
        fields = '__all__'

class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Proveedor  
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Producto  
        fields = '__all__'
    
    categoria_nombre = serializers.ReadOnlyField(source='categoria_fk.nombre')
    proveedor_nombre = serializers.ReadOnlyField(source='proveedor_fk.nombre')
    negocio_nombre = serializers.ReadOnlyField(source='negocio_fk.nombre')

# MODULO CLIENTE

class UbicacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ubicacion  
        fields = '__all__'

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cliente  
        fields = '__all__'
        
        
# MODULO ARCHIVOS

class ImagenSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Imagen  
        fields = '__all__'

class ImagenProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ImagenProducto  
        fields = '__all__'