from django.contrib import admin
from einkaufsliste_app.models import CustomList, ListItem, PurchasingItem

# Register your models here.
class PurchasingItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active']

class CustomListAdmin(admin.ModelAdmin):
    list_display = ['name']

class ListItemAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(PurchasingItem, PurchasingItemAdmin)
admin.site.register(CustomList, CustomListAdmin)
admin.site.register(ListItem, ListItemAdmin)

