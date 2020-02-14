from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('index/', views.index,name='index'),
    path('register/', views.register, name='register'),
    path('inventory/', views.inventory, name='inventory'),
]
