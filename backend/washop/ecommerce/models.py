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
    pais_id = models.ForeignKey(Pais, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.nombre}"

class Provincia(models.Model):
    nombre = models.CharField(max_length=100)
    departamento = models.ForeignKey(Departamento, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.nombre}"   
    
class Distrito(models.Model):
    nombre = models.CharField(max_length=100)
    provincia = models.ForeignKey(Provincia, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.nombre}"   

class Ubicacion(models.Model):
    direccion = models.CharField(max_length=150)
    referencia = models.CharField(max_length=150, blank=True, null=True)
    distrito = models.ForeignKey(Distrito, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.direccion}"    
    

# MODULO NEGOCIO

class Rubro(models.Model):
    nombre_rubro = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_rubro
    
class Rol(models.Model):
    nombre_rol = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre_rol

class Negocio(models.Model):
    pais = models.ForeignKey(Pais, on_delete=models.SET_NULL, null=True, blank=True)
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
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    negocio = models.ForeignKey(Negocio, on_delete=models.CASCADE)  # Asume que tienes un modelo 'Negocio'
    rol = models.ForeignKey(Rol, on_delete=models.SET_NULL, null=True)  # Asume que tienes un modelo 'Rol'

    def __str__(self):
        return f'{self.usuario.nombre} ({self.negocio.nombre}: {self.rol})'
    

# MODULO INVENTARIO

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre
    
class Proveedor(models.Model):
    nombre_proveedor = models.CharField(max_length=100)
    telefono = models.CharField(max_length=22, blank=True, null=True)
    correo = models.EmailField(max_length=100, blank=True, null=True)
    url = models.URLField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.nombre_proveedor

class Producto(models.Model):
    codigo = models.CharField(max_length=100, unique=True)
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    stock = models.PositiveIntegerField(blank=True, null=True)
    ubicacion = models.CharField(max_length=80, blank=True, null=True)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.SET_NULL, null=True)
    negocio = models.ForeignKey(Negocio, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre 

# MODULO ARHCIVOS

class Imagen(models.Model):
    url = models.URLField()

    
class ImagenProducto(Imagen):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    fecha_registro = models.DateTimeField(auto_now_add=True)


# MODULO CLIENTE

class Cliente(models.Model):
    nombre = models.CharField(max_length=64)
    apellido = models.CharField(max_length=64)
    telefono = models.CharField(max_length=22)  # Podría ser un campo de número de teléfono
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"



# MODULO INVENTARIO
class Marca(models.Model):
    nombre = models.CharField(max_length=64)
    
    def __str__(self):
        return f"{self.nombre}"


# VENTA


class EstadoVenta(models.Model):
    estado = models.CharField(max_length=64)
    
    def __str__(self):
        return f"{self.estado}"
    
    
class Venta(models.Model):
    estado = models.ForeignKey(EstadoVenta, on_delete=models.CASCADE)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)


