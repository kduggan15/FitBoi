from django.urls import path

from . import views

urlpatterns = [
    # ex: /fitboi_photo/
    path('', views.index, name='index'),
    path('submit/', views.submit, name='submit'),
    path('result/', views.result, name='result'),
]