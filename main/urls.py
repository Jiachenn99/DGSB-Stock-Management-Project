from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
<<<<<<< Updated upstream
    path(r'index/', views.index,name='index'),
    path(r'purchases/', views.purchases, name='purchases'),
    path(r'order/', views.order, name='order'),
    path(r'irrigation/', views.irrigation, name='irrigation'),
    path(r'plantation/', views.plantation, name='plantation'),
    path(r'vehicles/', views.vehicles, name='vehicles'),
    path(r'testing/', views.get_name, name='get_name'),
    path(r'addItem/<str:form_name>', views.addItem, name='addItem'),
=======
    path('index/', views.index,name='index'),
    path('register/', views.register, name='register'),
    path('userprofile/', views.userprofile, name='userprofile'),
    path('inventory/', views.inventory, name='inventory'),
>>>>>>> Stashed changes
]
