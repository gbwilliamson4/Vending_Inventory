from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('needed_inventory/', views.needed_inventory, name='needed_inventory'),
    path('to_buy/', views.to_buy, name='to_buy'),
]
