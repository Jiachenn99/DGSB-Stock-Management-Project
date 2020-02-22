from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('index/', views.index,name='index'),
    path('register/', views.register, name='register'),
    path('irrigation/', views.irrigation, name='irrigation'),
    path('plantation/', views.plantation, name='plantation'),
    path('vehicles/', views.vehicles, name='vehicles'),
]
