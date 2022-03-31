# Generated by Django 4.0.3 on 2022-03-22 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wms', '0002_remove_pedidos_cliente'),
        ('cat_wms', '0003_remove_producto_usuario'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Clientes',
        ),
        migrations.DeleteModel(
            name='Flotilla',
        ),
        migrations.RenameField(
            model_name='centro',
            old_name='descripcion',
            new_name='direccion',
        ),
        migrations.RemoveField(
            model_name='centro',
            name='nomenglatura',
        ),
        migrations.RemoveField(
            model_name='proveedor',
            name='direccion',
        ),
        migrations.RemoveField(
            model_name='proveedor',
            name='telefono2',
        ),
        migrations.AddField(
            model_name='proveedor',
            name='email',
            field=models.EmailField(default='hola@gmail.com', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='proveedor',
            name='rfc',
            field=models.CharField(blank=True, max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='centro',
            name='centro',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='centro',
            name='id',
            field=models.AutoField(db_column='centro_id', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='centro',
            name='sociedad',
            field=models.CharField(default='malifiestas', max_length=150),
            preserve_default=False,
        ),
        migrations.AlterModelTable(
            name='categoria',
            table='cat_producto_categoria',
        ),
        migrations.DeleteModel(
            name='Perfil',
        ),
        migrations.DeleteModel(
            name='Sociedad',
        ),
    ]
