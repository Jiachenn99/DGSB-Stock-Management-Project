from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('delete/<str:category>/<str:subcategory>/item_<pk>', views.delete_entry, name='deletion'),
    path('vehicle/<str:subcategory>', views.vehicle, name='vehicle'),
    path('Plantation_Tables/<str:subcategory>', views.plantation, name='plantation'),
    path('Irrigation_Tables/<str:subcategory>', views.irrigation, name='irrigation'),
    path('supplier/', views.supplier, name='supplier'),
    path(r'index/', views.index ,name='index'),
    path(r'purchases/', views.purchases, name='purchases'),
    path(r'order/', views.order, name='order'),
    path(r'addItem/<str:category>/<str:subcategory>', views.addItem, name='addItem'),
    path(r'userprofile/', views.userprofile, name='userprofile'),
    
]
