from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from core.views import *

urlpatterns = [
  path('', Index.as_view(), name='index'),
  # path('service/<int:id>/', service, name='service'),
  path('doctor/<int:id>/', doctor_page, name='doctor'),
  path('news/<int:id>/', news_page, name='news'),
  path('advice/<int:id>/', advice_page, name='advice'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
