# Generated by Django 4.0 on 2021-12-14 14:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cat_wms', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetalleEntrada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_entrada', models.DateTimeField(auto_now_add=True, null=True)),
                ('lote', models.CharField(blank=True, max_length=20, null=True)),
                ('cantidad', models.IntegerField(blank=True, null=True)),
                ('unidad', models.CharField(blank=True, max_length=10, null=True)),
                ('ubicacion', models.CharField(blank=True, max_length=20, null=True)),
                ('referencia', models.CharField(blank=True, max_length=30, null=True)),
                ('precio_compra', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('impresion_etiqueta', models.CharField(blank=True, max_length=10, null=True)),
                ('estatus', models.CharField(blank=True, default='ALTA', max_length=30, null=True)),
                ('estatus_entrada', models.CharField(blank=True, max_length=30, null=True)),
                ('almacen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cat_wms.almacenes')),
                ('centro', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cat_wms.centro')),
            ],
        ),
        migrations.CreateModel(
            name='Pedidos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(auto_now_add=True)),
                ('fecha_instalacion', models.DateField(blank=True, null=True, verbose_name='F. Instalación')),
                ('hora_instacion', models.TimeField(blank=True, null=True)),
                ('evento_fecha', models.DateField(blank=True, null=True)),
                ('evento_hora', models.TimeField(blank=True, null=True)),
                ('recoleccion_fecha', models.DateField(blank=True, null=True)),
                ('recoleccion_hora', models.TimeField(blank=True, null=True)),
                ('estatus', models.CharField(default='PRESUPUESTO', max_length=50)),
                ('lugar_entrega', models.TextField(blank=True, null=True)),
                ('tipo_pedido', models.CharField(blank=True, max_length=10, null=True)),
                ('anticipo', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('docfactura', models.FileField(blank=True, null=True, upload_to='facpedido')),
                ('docdocumento', models.FileField(blank=True, null=True, upload_to='dicpedido')),
                ('direccion', models.CharField(blank=True, max_length=255, null=True)),
                ('lat', models.DecimalField(blank=True, decimal_places=16, max_digits=22, null=True)),
                ('long', models.DecimalField(blank=True, decimal_places=16, max_digits=22, null=True)),
                ('iva', models.BooleanField(default=False)),
                ('surt_completado', models.BooleanField(default=False)),
                ('observaciones', models.TextField(blank=True, null=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clientes', to='cat_wms.perfil')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
            options={
                'ordering': ['-pk'],
            },
        ),
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_hora', models.DateTimeField(auto_now_add=True)),
                ('usuario', models.CharField(blank=True, max_length=50, null=True)),
                ('codigo', models.CharField(blank=True, max_length=20, null=True)),
                ('lote', models.CharField(blank=True, max_length=20, null=True)),
                ('cantidad', models.IntegerField(blank=True, null=True)),
                ('unidad', models.CharField(blank=True, max_length=30, null=True)),
                ('ubicacion', models.CharField(blank=True, max_length=20, null=True)),
                ('categoria', models.CharField(blank=True, max_length=30, null=True)),
                ('referencia', models.CharField(blank=True, max_length=100, null=True)),
                ('estatus', models.CharField(blank=True, max_length=20, null=True)),
                ('flag_surtiendo', models.IntegerField(blank=True, null=True)),
                ('almacen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cat_wms.almacenes')),
                ('centro', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cat_wms.centro')),
                ('detalle_entrada', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wms.detalleentrada')),
                ('producto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cat_wms.producto')),
            ],
        ),
        migrations.CreateModel(
            name='Entrada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_entrada', models.DateTimeField(auto_now_add=True)),
                ('transporte', models.CharField(blank=True, max_length=50, null=True)),
                ('operador', models.CharField(max_length=50)),
                ('capacidad', models.CharField(max_length=30)),
                ('placas', models.CharField(blank=True, max_length=10, null=True)),
                ('datos_adjuntos', models.CharField(blank=True, max_length=50, null=True)),
                ('observacion', models.CharField(blank=True, max_length=250, null=True)),
                ('estatus', models.CharField(blank=True, max_length=20, null=True)),
                ('f_arribo', models.DateTimeField(blank=True, null=True, verbose_name='Fecha Arribo')),
                ('f_descarga', models.DateTimeField(blank=True, null=True, verbose_name='Fecha Descarga')),
                ('centro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cat_wms.centro')),
                ('preveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cat_wms.proveedor')),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
        migrations.CreateModel(
            name='DetallePedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(blank=True, null=True)),
                ('observacion', models.CharField(blank=True, max_length=250, null=True)),
                ('cantidad_perdida', models.IntegerField(blank=True, null=True)),
                ('subtotal', models.FloatField(default=0)),
                ('recolectado', models.BooleanField(default=False)),
                ('cantidadrecuperada', models.SmallIntegerField(blank=True, null=True)),
                ('cantidadno_recuperada', models.SmallIntegerField(blank=True, null=True)),
                ('monto_acobrar', models.SmallIntegerField(blank=True, null=True)),
                ('reposicion_u', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('codigo', models.CharField(blank=True, max_length=7, null=True)),
                ('articulo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cat_wms.producto')),
                ('pedido', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pedido', to='wms.pedidos')),
            ],
        ),
        migrations.AddField(
            model_name='detalleentrada',
            name='entrada',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='wms.entrada'),
        ),
        migrations.AddField(
            model_name='detalleentrada',
            name='producto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cat_wms.producto'),
        ),
        migrations.AddField(
            model_name='detalleentrada',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.user'),
        ),
    ]