from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from upload.views import image_upload, minerData

urlpatterns = [
    path('', image_upload, name='upload'),
    path('admin/', admin.site.urls),
    path('json/', minerData, name="json"),
]

if not settings.USE_S3:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
