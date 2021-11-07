from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.main_view, name='main_view'),
    path('upload/', views.upload_image, name='upload_image'),
    path('list/', views.image_list, name='image_list'),
    path('crop/', views.crop, name='crop'),
    path('test/', views.test, name='test'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

