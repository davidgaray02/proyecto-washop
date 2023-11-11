from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from ecommerce import views

router = DefaultRouter()

router.register('usuario', views.UsuarioViewSet)

# MODULO NEGOCIO
router.register('rubro', views.RubroViewSet)
router.register('rol', views.RolViewSet)
router.register('negocio', views.NegocioViewSet)
router.register('usuario-negocio', views.UsuarioNegocioViewSet)

# MODULO INVENTARIO
router.register('proveedor', views.ProveedorViewSet)
router.register('categoria', views.CategoriaViewSet)
router.register('producto', views.ProductoViewSet)

# MODULO ARCHIVOS
router.register('imagen', views.CategoriaViewSet)
router.register('imagen-producto', views.NegocioViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
]
