from django.db import models

# Create your models here.

class PurchasingItem(models.Model):
    name = models.CharField(max_length=70)
    is_active = models.BooleanField(default=True)

class CustomList(models.Model):
    name = models.CharField(max_length=70)

class ListItem(models.Model):
    name = models.CharField(max_length=140)
    custom_list = models.ForeignKey(CustomList, on_delete=models.CASCADE)