# Generated by Django 4.0.3 on 2022-03-24 01:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cat_wms', '0005_remove_almacenes_state_remove_categoria_state_and_more'),
        ('wms', '0004_remove_inventario_categoria_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrada',
            name='id',
            field=models.AutoField(db_column='entrada_id', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='inventario',
            name='centro',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cat_wms.centro'),
        ),
        migrations.CreateModel(
            name='Ubicaciones',
            fields=[
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='Fecha de Modificación')),
                ('deleted_date', models.DateField(auto_now=True, verbose_name='Fecha de Eliminación')),
                ('id', models.AutoField(db_column='ubicacion_id', primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, null=True)),
                ('centro', models.ForeignKey(db_column='centro_id', on_delete=django.db.models.deletion.CASCADE, to='cat_wms.centro')),
            ],
            options={
                'db_table': 'dim_ubicaciones',
            },
        ),
        migrations.AlterField(
            model_name='inventario',
            name='ubicacion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='wms.ubicaciones'),
        ),
    ]
