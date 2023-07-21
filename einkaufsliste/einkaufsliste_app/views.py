import os
import requests
import datetime
import re
from decouple import config
from http.client import HTTPResponse
from django.shortcuts import render
from django.utils import timezone
from django.conf import settings
from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.decorators import action, api_view
from einkaufsliste_app.models import (
    CustomList,
    ListItem, 
    PurchasingItem, 
    PurchasingItemCategory,
    WasteEvent, 
    WeatherData,
    Recipe,
    Ingredient,
    IngredientName,
    BarCode
)
from einkaufsliste_app.serializers import (
    CustomListSerializer, 
    ListItemSerializer, 
    PurchasingItemSerializer, 
    WasteEventSerializer, 
    WeatherDataSerializer,
    RecipeSerializer,
    IngredientSerializer,
    BarCodeSerializer,
    PurchasingItemCategorySerializer
)

class PurchasingItemViewSet(viewsets.ModelViewSet):
    queryset = PurchasingItem.objects.filter(is_active=True)
    serializer_class = PurchasingItemSerializer

    def create(self, request, *args, **kwargs):
        item, created = PurchasingItem.objects.update_or_create(
            name=request.data['name'],
            defaults={'is_active': True, 'date_created': timezone.now().date()}
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

class PurchasingItemCategoryViewset(viewsets.ModelViewSet):
    queryset = PurchasingItemCategory.objects.all()
    serializer_class = PurchasingItemCategorySerializer

class CustomListViewSet(viewsets.ModelViewSet):
    queryset = CustomList.objects.all()
    serializer_class = CustomListSerializer

class ListItemViewSet(viewsets.ModelViewSet):
    queryset = ListItem.objects.all()
    serializer_class = ListItemSerializer

class WeatherDataViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = WeatherData.objects.all()
    serializer_class = WeatherDataSerializer
    
    def list(self, request):
        latest_data = WeatherData.objects.filter(data_type=1).latest('weather_date')
        if (timezone.now() - latest_data.data_received_date) > datetime.timedelta(hours=1):
            if settings.DEBUG:
                parameter = {
                    'lat': config('lat'),
                    'lon': config('lon'),
                    'appid': config('API_KEY'),
                    'lang': config('lang'),
                }
            else:
                parameter = {
                    'lat': os.getenv('lat'),
                    'lon': os.getenv('lon'),
                    'appid': os.getenv("API_KEY"),
                    'lang': os.getenv('lang'),
                }
            response = requests.get('https://api.openweathermap.org/data/2.5/weather', params=parameter)
            if response.status_code == 200:
                json_response = response.json()
                data = {
                    'data_type': 1,
                    'weather_id': json_response['weather'][0]['id'],
                    'description': json_response['weather'][0]['description'],
                    'temperature': json_response['main']['temp'],
                    'temperature_min': json_response['main']['temp_min'],
                    'temperature_max': json_response['main']['temp_max'],
                    'clouds': json_response['clouds']['all'],
                    'weather_date': datetime.datetime.fromtimestamp(json_response['dt'], timezone.utc),
                    'data_received_date': timezone.now()
                }
                serializer = WeatherDataSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
                return Response(serializer.data)
            else:
                return Response(response.json())
        else:
            serializer = WeatherDataSerializer(latest_data)
            return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def wetter_morgen(self, request):
        weather_data = get_weather_forecast_data(1)
        return Response(weather_data)

    
    @action(detail=False, methods=['get'])
    def wetter_uebermorgen(self, request):
        weather_data = get_weather_forecast_data(2)
        return Response(weather_data)

class BarcodeViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    queryset = BarCode.objects.all()
    serializer_class = BarCodeSerializer

    def create(self, request, *args, **kwargs):
        barcode = request.data.get('code', None)
        if barcode:
            try:
                barcode_object = BarCode.objects.get(code=barcode)
                item, created = PurchasingItem.objects.update_or_create(
                    name=barcode_object.purchasing_item.name,
                    defaults={'is_active': True}
                )
                serializer = PurchasingItemSerializer(item)
                return Response(serializer.data)
            except BarCode.DoesNotExist:
                return Response({'status': 'failure', 'message': 'unknown code', 'barcode': barcode})
        else:
            return Response('parameter "barcode" is required')
    
    @action(detail=False, methods=['post'])
    def add_barcode(self, request, pk=None):
        barcode = request.data.get('code', None)
        purchasing_item = request.data.get('purchasing_item', None)
        if barcode and purchasing_item:
            purchasing_item_object, created = PurchasingItem.objects.get_or_create(name=purchasing_item)
            barcode_object = BarCode.objects.create(code=barcode, purchasing_item=purchasing_item_object)
            serializer = PurchasingItemSerializer(purchasing_item_object)
            return Response(serializer.data)
        else:
            return Response('parameter "barcode" and "purchasing_item" are required')

class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    def create(self, request, *args, **kwargs):
        name = request.data['name']
        preparation = request.data['preparation']
        ingredients = request.data['ingredients']
        recipe = Recipe.objects.create(
            name = name,
            preparation = preparation 
        )
        for ingredient in ingredients:
            name, created = IngredientName.objects.get_or_create(name=ingredient['name'])
            Ingredient.objects.create(
                name = name,
                amount = ingredient['amount'],
                unit = ingredient['unit'],
                recipe = recipe                                                                                   
            )
        serializer = self.get_serializer(recipe)
        return Response(serializer.data)
    
    def list(self, request, *args, **kwargs):
        queryset = Recipe.objects.all()
        serializer = RecipeSerializer(queryset, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def random(self, request):
        item = Recipe.objects.order_by('?').first()
        serializer = RecipeSerializer(item)
        return Response(serializer.data)

class IngredientViewSet(viewsets.GenericViewSet):
    queryset = Ingredient.objects.none()
    serializer_class = IngredientSerializer

    def create(self, request, *args, **kwargs):
        name = request.data['name']
        amount = request.data['amount']
        unit = request.data.unit

def get_weather_forecast_data(days_ahead):
    now = timezone.now()
    try:
        latest_data = WeatherData.objects.filter(data_type=2).latest('weather_date')
    except WeatherData.DoesNotExist:
        weatherdatas = get_wether_forecast_data_from_api()
        if weatherdatas:
            weatherdatas = WeatherData.objects.bulk_create(weatherdatas)
            latest_data = WeatherData.objects.filter(data_type=2).latest('weather_date')
    forecast_timedelta = datetime.timedelta(days=days_ahead)
    if (timezone.now() - latest_data.data_received_date) > datetime.timedelta(hours=1):
        WeatherData.objects.filter(data_type=2).delete()
        weatherdatas = get_wether_forecast_data_from_api()
        # print("Weatherdatas from API", weatherdatas)
        if weatherdatas: 
            weatherdatas = WeatherData.objects.bulk_create(weatherdatas)
            # print("Weatherdata queryset", weatherdatas)
            weatherdatas = [weatherdata for weatherdata in weatherdatas if weatherdata.weather_date.date() == now.date() + forecast_timedelta]
            # print("Weatherdatas: ", weatherdatas)
            serializer = WeatherDataSerializer(weatherdatas, many=True)
            return serializer.data
    else:
        queryset = WeatherData.objects.filter(data_type=2, weather_date__date=now.date() + forecast_timedelta)
        serializer = WeatherDataSerializer(queryset, many=True)
        return serializer.data

def get_wether_forecast_data_from_api():
    if settings.DEBUG:
        parameter = {
            'lat': config('lat'),
            'lon': config('lon'),
            'appid': config('API_KEY'),
            'lang': config('lang'),
        }
    else:
        parameter = {
            'lat': os.getenv('lat'),
            'lon': os.getenv('lon'),
            'appid': os.getenv("API_KEY"),
            'lang': os.getenv('lang'),
        }
    response = requests.get('https://api.openweathermap.org/data/2.5/forecast', params=parameter)
    if response.status_code == 200:
        json_response = response.json()
        weather_data_list = json_response['list']
        now = timezone.now()
        weatherdatas = []
        for weather_data in weather_data_list:
            weather_date = datetime.datetime.fromtimestamp(weather_data['dt'], timezone.utc)
            if weather_date.date() - now.date() > datetime.timedelta(days=2):
                break
            else:
                weatherdata_object = WeatherData(
                    data_type = 2,
                    weather_id = weather_data['weather'][0]['id'],
                    description = weather_data['weather'][0]['description'],
                    temperature = weather_data['main']['temp'],
                    temperature_min = weather_data['main']['temp_min'],
                    temperature_max = weather_data['main']['temp_max'],
                    clouds = weather_data['clouds']['all'],
                    weather_date = weather_date,
                    data_received_date = now,
                    probability_of_rain = weather_data['pop']
                )
                weatherdatas.append(weatherdata_object)
        return weatherdatas
    else:
        return response.json()

@api_view()
def waste_events(request):
    queryset = WasteEvent.objects.filter(event_date__gte=timezone.now().date())[:5]
    serializer_class = WasteEventSerializer
    serializer = WasteEventSerializer(queryset, many=True)

    return Response(serializer.data)

@action(detail=False, methods=['get'])
def test(self, request):
    testvar += 1
    return Response(testvar)

def index(request):
    return render(request, 'index.html')

def einkaufsliste(request):
    return render(request, 'einkaufsliste/index.html')

def rezepte(request):
    return render(request, 'rezepte/index.html')