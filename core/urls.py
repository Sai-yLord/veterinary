from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from core.views import index, service, doctor, news, feedback, advice, rebot

urlpatterns = [
    path('', index, name='index'),
    path('service/<int:id>/', service, name='service'),
    path('doctor/<int:id>/', doctor, name='doctor'),
    path('news/<int:id>/', news, name='news'),
    path('advice/<int:id>/', advice, name='advice'),
    path('feedback/', feedback, name='feedback'),
    path('rebot/', rebot, name='rebot')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
