from django.contrib import admin
from account.models import Staff

admin.site.register(Staff)
# Register your models here.
admin.site.site_header = 'DurianGarden Admin'