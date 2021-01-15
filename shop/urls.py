from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.product_list, name='product_list'),
    path('product/<int:product_pk>/', views.product_detail, name='product_detail'),
    path('basket/', views.product_basket, name='product_basket'),
    path('product/<int:product_pk>/add_to_basket', views.add_to_basket, name='add_to_basket'),
    path('product_delete/<int:product_pk>', views.remove_from_basket, name='remove_from_basket'),
    path('product_remove/<int:product_pk>', views.remove_all_products, name='remove_all_products'),
    path('delete_all/', views.delete_all, name='delete_all'),
    path('order/', views.order, name='order'),
    path('orders_history/', views.orders_history, name='orders_history'),
    path('add_to_favorites/<int:product_pk>', views.add_to_favorites, name='add_to_favorites')


]
