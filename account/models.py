from django.db import models
from main.decorators import unauthenticated_user, allowed_users, admin_only
# Create your models here.
from django.contrib.auth.models import User
# Create your models here.

class Staff(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    name = models.CharField(max_length = 200, null = True)
    phone = models.CharField(max_length = 200, null = True)
    email = models.CharField(max_length = 200, null = True)
    profile_pic = models.ImageField(default = '../images/userprofile.jpg',null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add = True, null = True)

    def __str__(self):
        return self.name
