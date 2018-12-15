from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):

    user = models.OneToOneField(User ,on_delete=models.CASCADE)

    phone_number = models.IntegerField(max_length=255 , unique=True)
    delivery_address = models.CharField(max_length=255 , unique=True)
    profile_pic = models.ImageField(upload_to='customer/profile_pics' , blank=True)

    def __str__(self):
        return self.user.username
