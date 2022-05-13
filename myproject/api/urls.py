from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile', views.index, name='index'),
    path('products', views.index, name='index'),
    path('categories', views.index, name='index'),
]