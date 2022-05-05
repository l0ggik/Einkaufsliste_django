from django.shortcuts import render
from rest_framework import viewsets
from einkaufsliste_app.models import PurchasingItem
from einkaufsliste_app.serializers import PurchasingItemSerializer

class PurchasingItemViewSet(viewsets.ModelViewSet):
    queryset = PurchasingItem.objects.all()
    serializer_class = PurchasingItemSerializer
