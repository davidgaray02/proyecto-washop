from django.db import models

# MODULO USUARIO

class Usuario(models.Model):
    nombre = models.CharField(max_length=64)
    apellido = models.CharField(max_length=64)
    whatsapp = models.CharField(max_length=22)

    email = models.EmailField(unique=True, blank=False)  # El argumento blank=False hace que el campo sea obligatorio
    password = models.CharField(max_length=128, blank=False, null=False)

    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'
    
    

# MODULO LOCALIZACIONES

class Pais(models.Model):
    nombre = models.CharField(max_length=100)
    cod_telefonico = models.CharField(max_length=10)
    simbolo_moneda = models.CharField(max_length=5)

    def __str__(self):
        return f"{self.nombre}"    
    
class Departamento(models.Model):
    nombre = models.CharField(max_length=100)
    pais_fk = models.ForeignKey(Pais, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.nombre}"

class Provincia(models.Model):
    nombre = models.CharField(max_length=100)
    departamento_fk = models.ForeignKey(Departamento, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.nombre}"   
    
class Distrito(models.Model):
    nombre = models.CharField(max_length=100)
    provincia_fk = models.ForeignKey(Provincia, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.nombre}"   

class Ubicacion(models.Model):
    direccion = models.CharField(max_length=150)
    referencia = models.CharField(max_length=150, blank=True, null=True)
    distrito_fk = models.ForeignKey(Distrito, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.direccion}"    
    

# MODULO NEGOCIO

class Rubro(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
class Rol(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre

class Negocio(models.Model):
    pais_fk = models.ForeignKey(Pais, on_delete=models.SET_NULL, null=True, blank=True)
    nombre  = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    RUC = models.CharField(max_length=32, blank=True, null=True)
    
    whatsapp = models.CharField(max_length=22)
    fb_url = models.URLField(blank=True, null=True)
    ig_url = models.URLField(blank=True, null=True)
    tiktok_url = models.URLField(blank=True, null=True)
    logo_url = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return self.nombre
    
class UsuarioNegocio(models.Model):
    usuario_fk = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    negocio_fk = models.ForeignKey(Negocio, on_delete=models.CASCADE)  # Asume que tienes un modelo 'Negocio'
    rol_fk = models.ForeignKey(Rol, on_delete=models.SET_NULL, null=True)  # Asume que tienes un modelo 'Rol'

    def __str__(self):
        return f'{self.usuario_fk.nombre} ({self.negocio_fk.nombre}: {self.rol_fk.nombre})'
    


# MODULO INVENTARIO
class Marca(models.Model):
    nombre = models.CharField(max_length=64)
    
    def __str__(self):
        return f"{self.nombre}"

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre
    
class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=22, blank=True, null=True)
    correo = models.EmailField(max_length=100, blank=True, null=True)
    url = models.URLField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    codigo = models.CharField(max_length=100, unique=True)
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(blank=True, null=True)
    ubicacion = models.CharField(max_length=80, blank=True, null=True)
    categoria_fk = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    proveedor_fk = models.ForeignKey(Proveedor, on_delete=models.SET_NULL, null=True)
    negocio_fk = models.ForeignKey(Negocio, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre 

# MODULO ARHCIVOS

class Imagen(models.Model):
    url = models.URLField()

    
class ImagenProducto(Imagen):
    producto_fk = models.ForeignKey(Producto, on_delete=models.CASCADE)
    fecha_registro = models.DateTimeField(auto_now_add=True)


# MODULO CLIENTE

class Cliente(models.Model):
    nombre = models.CharField(max_length=64)
    apellido = models.CharField(max_length=64)
    telefono = models.CharField(max_length=22)  # Podría ser un campo de número de teléfono
    ubicacion_fk = models.ForeignKey(Ubicacion, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"



# VENTA


class EstadoVenta(models.Model):
    estado = models.CharField(max_length=64)
    
    def __str__(self):
        return f"{self.estado}"
    
    
class Venta(models.Model):
    estado_fk = models.ForeignKey(EstadoVenta, on_delete=models.CASCADE)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)


