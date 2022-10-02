from django.contrib import admin
from einkaufsliste_app.models import CustomList, ListItem, PurchasingItem, WasteEvent, WeatherData

# Register your models here.
class PurchasingItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active']

class CustomListAdmin(admin.ModelAdmin):
    list_display = ['name']

class ListItemAdmin(admin.ModelAdmin):
    list_display = ['name']

class WeatherDataAdmin(admin.ModelAdmin):
    pass

class WasteEventAdmin(admin.ModelAdmin):
    pass

admin.site.register(PurchasingItem, PurchasingItemAdmin)
admin.site.register(CustomList, CustomListAdmin)
admin.site.register(ListItem, ListItemAdmin)
admin.site.register(WeatherData, WeatherDataAdmin)
admin.site.register(WasteEvent, WasteEventAdmin)
