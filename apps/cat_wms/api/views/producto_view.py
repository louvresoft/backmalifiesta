
from rest_framework import viewsets, pagination
from rest_framework import status
from rest_framework.response import Response

from apps.cat_wms.api import serializers as srlzrs


class ProductoViewSet(viewsets.ModelViewSet):
    serializer_class = srlzrs.ProductoSerializer
    pagination_class = pagination.LimitOffsetPagination

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state=True)
        else:
            return self.get_serializer().Meta.model.objects.filter(state=True, id=pk).first()
