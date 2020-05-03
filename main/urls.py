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
    path('userprofile_s/', views.userprofile_static, name='userprofile_static'),
    path('order/', views.orderView, name='order'),
    path('download_csv/<str:subcategory>', views.download_csv, name='download_csv'),
]
