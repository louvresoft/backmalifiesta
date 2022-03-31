from apps.cat_wms.models import Centro, Proveedor, Producto, Almacenes
from apps.base.models import BaseModel
from apps.user.models import User
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver


ESTATUS_CHOICES = (
    ('LIBRE', 'LIBRE'),
    ('CUARENTENA', 'CUARENTENA'),
    ('RECHAZO', 'RECHAZO')
)


class Ubicaciones(BaseModel):
    id = models.AutoField(primary_key=True, db_column="ubicacion_id")
    nombre = models.CharField(max_length=100, null=True)
    centro = models.ForeignKey(Centro, on_delete=models.CASCADE, db_column="centro_id")

    class Meta:
        db_table = "dim_ubicaciones"


class Entrada(BaseModel):
    id = models.AutoField(primary_key=True, db_column="entrada_id")
    nombre = models.CharField(max_length=200)
    centro = models.ForeignKey(Centro, on_delete=models.CASCADE, db_column="centro_id")
    fecha_entrada = models.DateTimeField(auto_now_add=True)
    observaciones = models.TextField(blank=True, null=True)
    fecha_pedido = models.DateTimeField(blank=True, null=True)
    fecha_entregada = models.DateTimeField()
    datos_adjuntos = models.CharField(max_length=50, blank=True, null=True)  # ADJUNTA DOCUMENTOS
    estatus = models.CharField(choices=ESTATUS_CHOICES, default='LIBRE', blank=True, null=True, max_length=10)

    def __str__(self):
        return '{0}'.format(self.id)

    class Meta:
        db_table = "dim_entrada"


@receiver(pre_save, sender=Entrada)
def pre_save_user(sender, instance, **kwargs):
    if not instance._state.adding:
        print('this is an update')
    else:
        print('this is an insert')


class DetalleEntrada(BaseModel):
    id = models.AutoField(primary_key=True, db_column="detalle_entrada_id")
    entrada = models.ForeignKey(Entrada, on_delete=models.CASCADE, db_column="entrada_id")
    nombre = models.CharField(max_length=250, blank=True, null=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, blank=True, null=True)
    lote = models.CharField(max_length=20, blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)
    ubicacion = models.CharField(max_length=20, blank=True, null=True)
    referencia = models.CharField(max_length=100, blank=True, null=True)
    precio_compra = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    fecha_entrada = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    estatus = models.CharField(choices=ESTATUS_CHOICES, default='LIBRE', blank=True, null=True, max_length=10)
    estatus_entrada = models.CharField(choices=ESTATUS_CHOICES, default='LIBRE', blank=True, null=True, max_length=10)
    centro = models.ForeignKey(Centro, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.id

    class Meta:
        db_table = "det_entrada"


@receiver(pre_save, sender=DetalleEntrada)
def pre_save_user(sender, instance, **kwargs):
    if not instance._state.adding:
        print('this is an update')
    else:
        print('this is an insert')


class Inventario(BaseModel):
    id = models.AutoField(primary_key=True, db_column="inventario_id")
    detalle_entrada = models.ForeignKey(DetalleEntrada, on_delete=models.CASCADE, db_column="detalle_entrada_id")
    usuario = models.CharField(max_length=50, blank=True, null=True)
    codigo = models.CharField(max_length=20, blank=True, null=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, blank=True, null=True)
    lote = models.CharField(max_length=20, blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)
    unidad = models.CharField(max_length=30, blank=True, null=True)
    ubicacion = models.ForeignKey(Ubicaciones, null=True, on_delete=models.CASCADE)
    activo = models.BooleanField(default=False)
    centro = models.ForeignKey(Centro, on_delete=models.CASCADE, blank=True, null=True)
    almacen = models.ForeignKey(Almacenes, on_delete=models.CASCADE)
    flag_surtiendo = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.id

    class Meta:
        db_table = "dim_inventario"


class Pedidos(BaseModel):
    id = models.AutoField(primary_key=True, db_column="pedido_id")
    fecha = models.DateField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_instalacion = models.DateField("F. Instalación", blank=True, null=True)
    hora_instacion = models.TimeField(blank=True, null=True)
    evento_fecha = models.DateField(blank=True, null=True)
    evento_hora = models.TimeField(blank=True, null=True)
    recoleccion_fecha = models.DateField(blank=True, null=True)
    recoleccion_hora = models.TimeField(blank=True, null=True)
    estatus = models.CharField(max_length=50, default="PRESUPUESTO")
    #cliente = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name="clientes")
    lugar_entrega = models.TextField(blank=True, null=True)
    tipo_pedido = models.CharField(max_length=10, blank=True, null=True)
    anticipo = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    doc_factura = models.FileField(upload_to='facpedido', blank=True, null=True)
    doc_documento = models.FileField(upload_to='dicpedido', blank=True, null=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    lat = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    long = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    iva = models.BooleanField(default=False)
    surt_completado = models.BooleanField(default=False)
    observaciones = models.TextField(blank=True, null=True)

    class Meta:
        db_table = "dim_pedido"
        ordering = ['-pk']

    def __str__(self):
        return self.id


class DetallePedido(BaseModel):
    id = models.AutoField(primary_key=True, db_column="detalle_pedido_id")
    pedido = models.ForeignKey(Pedidos, on_delete=models.CASCADE, blank=True, null=True, related_name='pedido')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)
    observaciones = models.CharField(max_length=250, blank=True, null=True)
    cantidad_perdida = models.IntegerField(blank=True, null=True)
    cantidad_recuperada = models.SmallIntegerField(blank=True, null=True)
    monto_acobrar = models.SmallIntegerField(blank=True, null=True)

    def __str__(self):
        return self.articulo

    class Meta:
        db_table = "det_pedido"

    def total_linea(self):
        return self.articulo.precio_renta * self.cantidad

    def reposicion(self):
        return self.articulo.reposicion

    def cod(self):
        return self.articulo.codigo

    def recoleccion(self):
        if self.cantidadrecuperada != None:
            if self.cantidad > self.cantidadrecuperada:
                print("hacemos resta")
                resta = self.cantidad - self.cantidadrecuperada
                print(resta)
                a = self.cantidadno_recuperada = resta
                return a

    def save(self, **kwargs):
        self.reposicion_u = self.reposicion()
        self.subtotal = float(float(int(self.cantidad)) * float(self.articulo.precio_renta))
        self.cantidadno_recuperada = self.recoleccion()
        self.codigo = self.cod()
        # self.monto_acobrar = self.montoacobrar()
        super(DetallePedido, self).save()


class Salida(BaseModel):
    id = models.AutoField(primary_key=True, db_column="salida_id")
    pedido = models.ForeignKey(Pedidos, on_delete=models.CASCADE)
    operador = models.CharField(max_length=50)
    tipo_unidad = models.CharField(max_length=100, null=True)
    placas = models.CharField(max_length=20, null=True)
    observaciones = models.CharField(max_length=20, null=True)
    fecha_salida = models.DateTimeField(null=True)

    class Meta:
        db_table = "dim_salida"


class Retorno(BaseModel):
    id = models.AutoField(primary_key=True, db_column="retorno_id")
    nombre = models.CharField(max_length=200)
    operador = models.CharField(max_length=100)
    tipo_unidad = models.CharField(max_length=50, null=True)
    placas = models.CharField(max_length=20, null=True)
    observaciones = models.TextField()
    fecha_reingreso = models.DateField(null=True)

    class Meta:
        db_table = "dim_retorno"

