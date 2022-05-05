from rest_framework import serializers
from einkaufsliste_app.models import PurchasingItem

class PurchasingItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchasingItem
        fields = '__all__'
