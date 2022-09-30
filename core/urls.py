
from django.contrib import admin
from django.urls import path
from products.views import products_view, product_view, product_add_view, product_delete_view, product_edit_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', products_view, name='products'),
    path('product/<int:pk>/', product_view, name='product'),
    path('product/add/', product_add_view, name='product_add'),
    path('product/edit/<int:pk>', product_edit_view, name='product_edit'),
    path('product/delete/<int:pk>', product_delete_view, name='product_delete'),
]
