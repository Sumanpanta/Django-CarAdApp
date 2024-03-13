from django.db import models
from django.contrib.auth.models import User

from localflavor.us.models import USStateField, USZipCodeField

class Location(models.Model):
    address_1 = models.CharField(max_length=128, blank = True)
    address_2 = models.CharField(max_length=128, blank = True)
    city = models.CharField(max_length = 60)
    state= USStateField(default = "NY")
    zipcode = USZipCodeField(blank = True)
    
    def __str__(self):
        return f' Location {self.id}'
    

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(null=True)
    bio = models.CharField(max_length=150, blank = True)
    phone_number = models.CharField(max_length=12, blank = True)
    Location = models.OneToOneField(Location, on_delete=models.SET_NULL, null = True)
    
#on_delete rakhyo vani if profile gets deleted, location deleted too
    
    
    def __str__(self):
        return f'{self.user.username}\'s Profile'
    
#for localflavor: goto:setting.py src, add into installed_app

