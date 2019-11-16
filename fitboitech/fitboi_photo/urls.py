from django.urls import path

from . import views

urlpatterns = [
    # ex: /fitboi_photo/
    path('', views.index, name='index'),
]