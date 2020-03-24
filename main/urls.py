from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('index/', views.index,name='index'),
    path('purchases/', views.purchases, name='purchases'),
    path('order/', views.order, name='order'),
    path('irrigation/', views.irrigation, name='irrigation'),
    path('plantation/', views.plantation, name='plantation'),
    path('vehicles/', views.vehicles, name='vehicles'),
    path('testing/', views.get_name, name='get_name'),
    path('addItem/<str:form_name>', views.addItem, name='addItem'),
]
