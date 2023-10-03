from django.urls import path
from app_task3 import views


urlpatterns = [
    path('', views.app_task3, name='app_task3'),
    path('basket/<int:user_id>/', views.basket, name='basket'),
    path('sorted_basket/<int:user_id>/<int:days_ago>/', views.sorted_basket, name='sorted_basket'),

]
