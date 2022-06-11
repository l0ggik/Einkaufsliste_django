from django.contrib import admin
from einkaufsliste_app.models import PurchasingItem

# Register your models here.
class PurchasingItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active']

admin.site.register(PurchasingItem, PurchasingItemAdmin)

