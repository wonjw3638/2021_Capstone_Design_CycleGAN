from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.main_view, name='main_view'),
    path('select/', views.select, name='select'),
    path('day/', views.day, name='day'),
    path('night/', views.night, name='night'),
    path('spring/', views.spring, name='spring'),
    path('summer/', views.summer, name='summer'),
    path('autumn/', views.autumn, name='autumn'),
    path('winter/', views.winter, name='winter'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

