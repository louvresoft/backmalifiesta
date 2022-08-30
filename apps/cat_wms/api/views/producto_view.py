
from rest_framework import viewsets, pagination
from rest_framework import status
from rest_framework.response import Response

from apps.cat_wms.api import serializers as srlzrs


class ProductoViewSet(viewsets.ModelViewSet):
    serializer_class = srlzrs.ProductoSerializer
    pagination_class = pagination.LimitOffsetPagination

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        else:
            return self.get_serializer().Meta.model.objects.filter(id=pk).first()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
