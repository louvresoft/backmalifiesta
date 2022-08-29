from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static


from apps.urls import urlpatterns as api_urls_v1


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(api_urls_v1)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
