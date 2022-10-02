"""einkaufsliste URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from einkaufsliste_app.views import CustomListViewSet, ListItemViewSet, PurchasingItemViewSet, WeatherDataViewSet,waste_events, einkaufsliste, index, rezepte

router = routers.DefaultRouter()
router.register(r'einkauf', PurchasingItemViewSet)
router.register(r'wetter', WeatherDataViewSet)
router.register(r'lists', CustomListViewSet)
router.register(r'list_items', ListItemViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', index, name='index'),
    path('einkaufsliste/', einkaufsliste, name='einkaufsliste'),
    path('rezepte/', rezepte, name='rezepte'),
    path('api/muell/', waste_events, name='waste_events')
]
