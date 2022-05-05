from django.db import models

# Create your models here.

class PurchasingItem(models.Model):
    name = models.CharField(max_length=70)
