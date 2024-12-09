from django.db import models
from django.contrib.auth.models import AbstractUser, Group

class Customer(AbstractUser):
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

def create_user_groups():
    admin_group, created = Group.objects.get_or_create(name='Admin')
    seller_group, created = Group.objects.get_or_create(name='Seller')
    customer_group, created = Group.objects.get_or_create(name='Customer')
    
    if created:
        print("Groups created successfully!")
    else:
        print("Groups already exist.")

from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    class Meta:
        permissions = [
            ("can_add_product", "Can add product"),
            ("can_edit_product", "Can edit product"),
            ("can_delete_product", "Can delete product"),
        ]
