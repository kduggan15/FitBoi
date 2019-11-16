from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from .views import *

from . import views

urlpatterns = [
    # ex: /fitboi_photo/
    path('', views.index, name='index'),
    path('upload', user_image_view, name='image_upload'),
    path('success', success, name='success'),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
