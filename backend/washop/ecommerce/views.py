from django.shortcuts import render
from rest_framework import viewsets
from . import serializers, models

# Create your views here.

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = models.Usuario.objects.all()
    serializer_class = serializers.UsuarioSerializer

# MODULO NEGOCIO

class RubroViewSet(viewsets.ModelViewSet):
    queryset = models.Rubro.objects.all()
    serializer_class = serializers.RubroSerializer

class RolViewSet(viewsets.ModelViewSet):
    queryset = models.Rol.objects.all()
    serializer_class = serializers.RolSerializer

class NegocioViewSet(viewsets.ModelViewSet):
    queryset = models.Negocio.objects.all()
    serializer_class = serializers.NegocioSerializer

class UsuarioNegocioViewSet(viewsets.ModelViewSet):
    queryset = models.UsuarioNegocio.objects.all()
    serializer_class = serializers.UsuarioNegocioSerializer


# MODULO INVENTARIO

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = models.Categoria.objects.all()
    serializer_class = serializers.CategoriaSerializer

class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = models.Proveedor.objects.all()
    serializer_class = serializers.ProveedorSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = models.Producto.objects.all()
    serializer_class = serializers.ProductoSerializer



# MODULO CLIENTE

class UbicacionViewSet(viewsets.ModelViewSet):
    queryset = models.Ubicacion.objects.all()
    serializer_class = serializers.UbicacionSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = models.Cliente.objects.all()
    serializer_class = serializers.ClienteSerializer
    

# MODULO ARCHIVO

class ImagenViewSet(viewsets.ModelViewSet):
    queryset = models.Imagen.objects.all()
    serializer_class = serializers.ImagenSerializer

class ImagenProductoViewSet(viewsets.ModelViewSet):
    queryset = models.ImagenProducto.objects.all()
    serializer_class = serializers.ImagenProductoSerializer
