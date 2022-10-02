from rest_framework import serializers
from einkaufsliste_app.models import CustomList, ListItem, PurchasingItem, WasteEvent, WeatherData

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
