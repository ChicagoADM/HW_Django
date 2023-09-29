"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from app_task2 import views



users_patterns = [
    path('', views.user_read, name='users'),
    path('create/', views.user_create, name='user_create'),
    path('update/', views.user_update, name='user_update'),
    path('delete/', views.user_delete, name='user_delete'),
]

products_patterns = [
    path('', views.product_read, name='products'),
    path('create/', views.product_create, name='product_create'),
    path('update/', views.product_update, name='product_update'),
    path('delete/', views.product_delete, name='product_delete'),
]

orders_patterns = [
    path('', views.order_read, name='orders'),
    path('create/', views.order_create, name='order_create'),
    path('update/', views.order_update, name='order_update'),
    path('delete/', views.order_delete, name='order_delete'),
]

urlpatterns = [
    path('', views.app_task2, name='app_task2'),
    path('users/', include(users_patterns)),
    path('products/', include(products_patterns)),
    path('orders/', include(orders_patterns)),
]
