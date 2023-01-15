from django.conf import settings
User = settings.AUTH_USER_MODEL
from django.contrib.auth.models import AbstractUser
from django.db import models



# Create your models here.

class CustomUser(AbstractUser):
    name_first = models.CharField(default="", max_length=100)
    name_last = models.CharField(default="", max_length=100)
    phone_number = models.CharField(default="", max_length=100)
    name_of_company = models.CharField(default="", max_length=100)
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name_first = models.CharField(default="", max_length=100)
    name_last = models.CharField(default="", max_length=100)
    phone_number = models.CharField(default="", max_length=100)
    name_of_company = models.CharField(default="", max_length=100)



    def save(self, *args, **kwargs):
        self.name_first = self.user.name_first
        self.name_last = self.user.name_last
        self.phone_number = self.user.phone_number
        self.name_of_company = self.user.name_of_company


        super().save(*args, **kwargs)
    

    def __str__(self):
        return f'{self.user.username} Profile'



    

