from django.urls import path
from . import views
from django.contrib import admin

app_name = 'main'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('delete/<str:category>/<str:subcategory>/item_<pk>', views.delete_entry, name='deletion'),
    path('Vehicle_Tables/<str:subcategory>', views.vehicle, name='vehicle'),
    path('updateItem/<str:category>/<str:subcategory>/item_<pk>', views.update_entry, name='update'),
    path('Plantation_Tables/<str:subcategory>', views.plantation, name='plantation'),
    path('Irrigation_Tables/<str:subcategory>', views.irrigation, name='irrigation'),
    path('supplier/', views.supplier, name='supplier'),
    path('index/', views.index ,name='index'),
    path('addItem/<str:category>/<str:subcategory>', views.addItem, name='addItem'),
    path('purchasing/', views.purchasing, name='purchasing'),
    path('userprofile/', views.userprofile, name='userprofile'),
    path('order/', views.orderView, name='order'),
    path('success/', views.successView, name='success'),

]
