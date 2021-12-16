from rest_framework import serializers
from apps.cat_wms.models import Producto


class ProductoSerializer(serializers.ModelSerializer):
    alto = serializers.IntegerField()
    piezas_caja = serializers.IntegerField(required=False)
    maximo = serializers.IntegerField(required=False)

    class Meta:
        model = Producto
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')
