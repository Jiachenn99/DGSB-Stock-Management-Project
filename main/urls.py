from django.urls import path
from . import views
from django.contrib import admin

app_name = 'main'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('delete/<str:category>/<str:subcategory>/item_<pk>', views.delete_entry, name='deletion'),
    path('update/<str:category>/<str:subcategory>/item_<pk>', views.update_entry, name='update'),
    path('vehicle/<str:subcategory>', views.vehicle, name='vehicle'),
    path('Plantation_Tables/<str:subcategory>', views.plantation, name='plantation'),
    path('Irrigation_Tables/<str:subcategory>', views.irrigation, name='irrigation'),
    path('supplier/', views.supplier, name='supplier'),
    path(r'index/', views.index ,name='index'),
    path(r'addItem/<str:category>/<str:subcategory>', views.addItem, name='addItem'),
    path(r'purchasing/', views.purchasing, name='purchasing'),
    path(r'userprofile/', views.userprofile, name='userprofile'),
    path('order/', views.orderView, name='order'),
    path('success/', views.successView, name='success'),

]
