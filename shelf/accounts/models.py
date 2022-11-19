from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class UserAddress(models.Model):

    name = models.CharField(max_length=250, db_index=True)
    province = models.CharField(max_length=250, db_index=True)
    district = models.CharField(max_length=250, db_index=True)
    street = models.CharField(max_length=250, db_index=True)


class CustomUser(AbstractUser):

    address = models.ForeignKey(UserAddress, on_delete=models.CASCADE)
    phone = models.CharField(max_length=250, db_index=True)

