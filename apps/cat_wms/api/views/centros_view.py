from rest_framework import viewsets, pagination
from apps.cat_wms.api import serializers as srlzrs


class CentroViewSet(viewsets.ModelViewSet):
    serializer_class = srlzrs.CentroSerializer
    pagination_class = pagination.LimitOffsetPagination

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all().order_by('-id')
        else:
            return self.get_serializer().Meta.model.objects.filter(id=pk).first()
