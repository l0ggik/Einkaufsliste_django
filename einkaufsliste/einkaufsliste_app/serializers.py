from rest_framework import serializers
from einkaufsliste_app.models import (
    CustomList, 
    ListItem, 
    PurchasingItem, 
    WasteEvent, 
    WeatherData,
    Recipe,
    Ingredient
)

class PurchasingItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchasingItem
        fields = '__all__'

class CustomListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomList
        fields = '__all__'

class ListItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListItem
        fields = '__all__'

class WeatherDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherData
        fields = '__all__'

class WasteEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = WasteEvent
        fields = '__all__'


class IngredientSerializer(serializers.ModelSerializer):
    name = serializers.StringRelatedField()
    class Meta:
        model = Ingredient
        fields = ['name', 'amount', 'get_unit_display']

class RecipeSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True, read_only=True)
    class Meta:
        model = Recipe
        fields = ['name', 'preparation', 'ingredients']

