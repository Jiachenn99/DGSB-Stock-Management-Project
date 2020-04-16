from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('delete/<label>/item_<pk>', views.delete_entry, name='deletion'),
    path('vehicle/<str:table>', views.vehicle, name='vehicle'),
    path('plantation/<str:table>', views.plantation, name='plantation'),
    path('irrigation/<str:table>', views.irrigation, name='irrigation'),
    path('supplier/', views.supplier, name='supplier'),
    path(r'index/', views.index,name='index'),
    path(r'purchases/', views.purchases, name='purchases'),
    path(r'order/', views.order, name='order'),
    path(r'addItem/<str:form_name>', views.addItem, name='addItem'),
    path(r'userprofile/', views.userprofile, name='userprofile'),
    
]
