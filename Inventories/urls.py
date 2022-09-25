from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('needed_inventory/', views.needed_inventory, name='needed_inventory'),
    path('to_buy/', views.to_buy, name='to_buy'),
    path('to_buy/<int:pk>/purchased/', views.purchased, name='purchased'),
    path('needed_inventory/<int:pk>/approve/', views.approve, name='approve'),
    path('needed_inventory/<int:pk>/delete/', views.delete, name='delete'),
    path('purchase_history', views.purchase_history, name='purchase_history'),
]
