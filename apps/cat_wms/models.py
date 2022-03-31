from apps.user.models import User
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.validators import MinLengthValidator

from apps.base.models import BaseModel


class Ubicaciones(BaseModel):
    ubicacion = models.CharField(max_length=5, unique=True)

    def __str__(self):
        return self.ubicacion

    class Meta:
        db_table = 'cat_ubicaciones'



class Centro(BaseModel):
    id = models.AutoField(primary_key=True, db_column="centro_id")
    sociedad = models.CharField(max_length=150)
    centro = models.CharField(max_length=150)
    direccion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nomenglatura

    class Meta:
        db_table = 'cat_centro'


class Almacenes(BaseModel):
    almacen = models.CharField(max_length=100)
    nomenglatura = models.CharField(max_length=10)
    centro = models.ForeignKey(Centro, on_delete=models.CASCADE)

    def __str__(self):
        return self.nomenglatura

    class Meta:
        db_table = 'cat_almacenes'


class Categoria(BaseModel):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'cat_producto_categoria'


class Proveedor(BaseModel):
    nombre = models.CharField(max_length=200)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField()
    rfc = models.CharField(max_length=13, blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'cat_provedores'


CAPACIDAD_CHOICES = (
    ('1.5 TON', '1.5 TON'),
    ('3.5 TON', '3.5 TON'),
    ('8.0 TON', '8.0 TON'),
)




PRODUCTOS_ESTATUS = (
    ('LIBERADO', 'LIBERADO'),
    ('MANTENIMIENDO', 'MANTENIMIENTO'),
    ('BAJA', 'BAJA')
)


class Producto(BaseModel):
    nombre = models.CharField("Clave", max_length=50, unique=True)
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    fecha_alta = models.DateTimeField(auto_now_add=True)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    codigo = models.CharField(max_length=7, validators=[MinLengthValidator(7)])
    modelo = models.CharField(max_length=50, blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    precio_compra = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    ganancia = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    precio_renta = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    precio_renta_mayoreo = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    reposicion = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    departamento = models.CharField(max_length=50, blank=True, null=True)
    imagen_frontal = models.ImageField(upload_to='img_producto', blank=True, null=True)
    imagen_lateral = models.ImageField(upload_to='img_producto', blank=True, null=True)
    imagen_posterior = models.ImageField(upload_to='img_producto', blank=True, null=True)
    codigo_barras = models.CharField(max_length=50, blank=True, null=True)
    alto = models.IntegerField(blank=True, null=True)
    largo = models.IntegerField(blank=True, null=True)
    ancho = models.IntegerField(blank=True, null=True)
    volumen_cm3 = models.IntegerField(blank=True, null=True)
    peso_g = models.IntegerField(blank=True, null=True)
    pais_origen = models.CharField(max_length=50, blank=True, null=True)
    piezas_caja = models.IntegerField(blank=True, null=True)
    piezas_tarima = models.IntegerField(blank=True, null=True)
    clasificacion = models.CharField(max_length=50, blank=True, null=True)
    observacion = models.CharField(max_length=120, blank=True, null=True)
    es_kit = models.BooleanField(default=False)
    maximo = models.IntegerField(blank=True, null=True)
    minimo = models.IntegerField(blank=True, null=True)
    estatus = models.CharField(max_length=20, choices=PRODUCTOS_ESTATUS)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'cat_producto'


