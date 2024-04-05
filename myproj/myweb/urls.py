from django.urls import path # для определения шаблонов
from myweb import views
from .views import create_client,create_order,create_product

urlpatterns = [
    # path('', views.home, name='home'),
    # path('info/', views.info_about_me, name='info_about_me'),
    
    path('client/', views.create_client, name='client-view'),
    path('product/', views.create_product, name='create_product'),
    path('order/', views.create_order, name='create_order'),
]