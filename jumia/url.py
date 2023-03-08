

from django.conf import settings
from django.urls import path, include
from jumia.views import download,Homeview



urlpatterns = [
    path('', Homeview, name='home'),
    path('download', download, name='download'),
]
# if settings.DEBUG:
    # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
