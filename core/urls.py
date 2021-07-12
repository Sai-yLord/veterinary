from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from core.views import index, service, doctor, new

urlpatterns = [
    path('', index, name='index'),
    path('service/<int:id>/', service, name='service'),
    path('doctor/<int:id>/', doctor, name='doctor'),
    path('news/<int:id>/', new, name='news'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
