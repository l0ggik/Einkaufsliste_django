from crypt import methods
from http.client import HTTPResponse
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from einkaufsliste_app.models import PurchasingItem
from einkaufsliste_app.serializers import PurchasingItemSerializer

class PurchasingItemViewSet(viewsets.ModelViewSet):
    queryset = PurchasingItem.objects.filter(is_active=True)
    serializer_class = PurchasingItemSerializer

    def create(self, request, *args, **kwargs):
        item, created = PurchasingItem.objects.update_or_create(
            name=request.data['name'],
            defaults={'is_active': True}
        )
        serializer = self.get_serializer(item)
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        item = PurchasingItem.objects.get(id=request.data)
        item.is_active = False
        item.save()
        serializer = PurchasingItemSerializer(item)
        return Response(serializer.data)
    
    @action(detail=False, methods=['delete'])
    def remove_all(self, request):
        queryset = PurchasingItem.objects.filter(is_active=True)
        updated_rows = queryset.update(is_active=False)
        return Response(updated_rows)

def index(request):
    return render(request, 'index.html')

def einkaufsliste(request):
    return render(request, 'einkaufsliste.html')
