from django.contrib import admin
from einkaufsliste_app.models import (
    CustomList, 
    ListItem, 
    PurchasingItem, 
    WasteEvent, 
    WeatherData, 
    Recipe, 
    Ingredient, 
    IngredientName, 
    Category, 
    BarCode,
    PurchasingItemCategory
)

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

class RecipeAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name', 'number']

class IngredientAdmin(admin.ModelAdmin):
    list_display = ['amount', 'unit']

class IngredientNameAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    pass

class BarCodeAdmin(admin.ModelAdmin):
    pass

class PurchasingItemCategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(PurchasingItem, PurchasingItemAdmin)
admin.site.register(CustomList, CustomListAdmin)
admin.site.register(ListItem, ListItemAdmin)
admin.site.register(WeatherData, WeatherDataAdmin)
admin.site.register(WasteEvent, WasteEventAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(IngredientName, IngredientNameAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(BarCode, BarCodeAdmin)
admin.site.register(PurchasingItemCategory, PurchasingItemCategoryAdmin)
