from django.urls import path, include

from apps.cat_wms.api import routers as  routers

urlpatterns = []

urlpatterns += [
    path("cat/", include(routers))
]