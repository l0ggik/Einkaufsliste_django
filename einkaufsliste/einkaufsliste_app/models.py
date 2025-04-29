from datetime import datetime
from django.db import models

# Create your models here.

class PurchasingItem(models.Model):
    name = models.CharField(max_length=70, unique=True)
    is_active = models.BooleanField(default=True)
    date_created = models.DateField(blank=True, null=True, default=None)
    category = models.ForeignKey('PurchasingItemCategory', default=None, null=True, blank=True, on_delete=models.CASCADE)
    supplier = models.ForeignKey('Supplier', default=None, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ['category__priority']

class PurchasingItemCategory(models.Model):
    name = models.CharField(max_length=70)
    priority = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return self.name
    
class Supplier(models.Model):
    name = models.CharField(max_length=70, unique=True)


class CustomList(models.Model):
    name = models.CharField(max_length=70)

class ListItem(models.Model):
    name = models.CharField(max_length=140)
    custom_list = models.ForeignKey(CustomList, on_delete=models.CASCADE)

class WeatherData(models.Model):
    CURRENT_WEATHER = 1
    FORECAST_WEATHER = 2
    DATA_TYPE_CHOICES = [
        (CURRENT_WEATHER, 'current weather'),
        (FORECAST_WEATHER, 'forecast weather')
    ]
    N = 1
    NNO = 2
    O = 3
    OSO = 4
    S = 5
    WSW = 6
    W = 7
    WNW = 8
    WIND_DIRECTION_CHOICES = [
        (N, 'Nord'),
        (NNO, 'Nord Nordost'),
        (O, 'Ost'),
        (OSO, 'Ost Südost'),
        (S, 'Süd'),
        (WSW, 'West Südwest'),
        (W, 'West'),
        (WNW, 'West Nordwest')
    ]
    data_type = models.PositiveSmallIntegerField(choices=DATA_TYPE_CHOICES)
    weather_id = models.PositiveSmallIntegerField()
    description = models.CharField(max_length=140)
    temperature = models.DecimalField(max_digits=6, decimal_places=2)
    temperature_min = models.DecimalField(max_digits=6, decimal_places=2)
    temperature_max = models.DecimalField(max_digits=6, decimal_places=2)
    clouds = models.PositiveSmallIntegerField()
    weather_date = models.DateTimeField()
    data_received_date = models.DateTimeField()
    probability_of_rain = models.DecimalField(max_digits=4, decimal_places=2, null=True, default=None, blank=True)
    wind_speed = models.DecimalField(max_digits=5, decimal_places=1, null=True, default=None, blank=True)
    wind_dir = models.PositiveSmallIntegerField(choices=WIND_DIRECTION_CHOICES, default=None, null=True, blank=True)
    pressure = models.DecimalField(max_digits=5, decimal_places=1, null=True, default=None, blank=True)
    precip = models.DecimalField(max_digits=5, decimal_places=1, null=True, default=None, blank=True)
    humidity = models.PositiveSmallIntegerField(null=True, default=None, blank=True)
    feelslike = models.DecimalField(max_digits=3, decimal_places=1, null=True, default=None, blank=True)
    uv = models.DecimalField(max_digits=4, decimal_places=1, null=True, default=None, blank=True)
    gust = models.DecimalField(max_digits=4, decimal_places=1, null=True, default=None, blank=True)

    def __str__(self):
        return self.description

class WasteEvent(models.Model):
    name = models.CharField(max_length=140)
    event_date = models.DateField()

    def __str__(self):
        return self.name
    class Meta:
        ordering = ['event_date']

    
    
class Recipe(models.Model):
    name = models.CharField(max_length=140, default='')
    preparation = models.TextField()
    categories = models.ManyToManyField('Category')
    number = models.PositiveIntegerField(unique=True, blank=True, null=True)
    # ingredients = models.ForeignKey('Ingredient', on_delete=models.RESTRICT)

class Category(models.Model):
    name = models.CharField(max_length=140, default='')

class Ingredient(models.Model):
    KILOGRAM = 1
    PIECES = 2
    GRAM = 3
    TABLESPOON = 4
    TEASPOON = 5
    MILILITER = 6
    NO_UNIT = 7
    SOME = 8
    LITER = 9
    PACKS = 10
    HAND_FULL = 11
    STEM = 12 # Stängel
    KNIFE_TIP = 13 # Messerspitze
    BUNCH = 14 # Bund
    PINCH = 15 # Prise
    STICK = 16 # Stange
    CAN = 17
    CANS = 18
    STEMS = 19 # Stiele
    SLICES = 20
    TWIGS = 21
    TUBERS = 22 # Knollen
    THICK = 23 # dicke
    SPLASHES = 24 # Spritzer
    LEAVES = 25
    CUBES = 26
    TWIG = 27
    PACK = 28 # Packung
    PLATE = 29
    STICKS = 30
    BALL = 31
    BOX = 32 # Kästchen
    SHEETS = 33
    PACKAGES = 34 # Päckchen
    SLICE = 35
    GLASS = 36
    PINCHES = 37 # Prisen
    BAG = 38 # Tüte
    SMALL = 39 # kleine
    SMALLER = 40 # kleiner
    PANICLE = 41 # Rispe
    HEAD = 42
    PAIR = 43
    BED = 44 # Beet
    CLOVE = 45
    PANICLES = 46 # Rispen
    BALLS = 47
    LEAVE = 48
    STEM = 49 # Stiel
    PODS = 50 # Schoten
    FLAKES = 51 # Plättchen
    CUP = 52
    GREAT = 53
    CM = 54
    HEADS = 55
    BOTTLE = 56
    LONG = 57 # lange
    YOUNG = 58
    SACHETS = 59 # Tütchen
    POUCH = 60 # Beutel
    LACING = 61 # Schuss
    MEDIUM_SIZED = 62 # mittelgroße
    COOKING_BAG = 63
    LITTLE_TIN = 64 # Döschen
    TUBER = 65 # Knolle
    DROP = 66 
    M = 67
    RING = 68
    CUPS = 69
    PACKAGE = 70
    DROPS = 71
    SHRUB = 72
    CLOVES = 73
    FULL = 74
    BEDS = 75 # Beete
    ROLLS = 76
    SMALLER = 77
    CL = 78
    LEAN = 79
    JARS = 80
    STRIPES = 81
    PORTION = 82
    MUG = 83 # Tasse 
    ROLL = 84
    BLOCKS = 85
    SHRUBS = 86
    PLATES = 87 # Platten
    HERB_BOUQUET = 88
    SPIKES = 89 # Zacken
    HERBAGE_BUNDLE = 90 # Kräuterbund
    HANDS_FULL = 91
    BOWLS = 92 # Schalen
    POTTY = 93 # Töpfchen
    RINGS = 94
    MOULDS = 95 # Förmchen
    VIALS = 96  # Fläschchen
    BAR = 97    # Tafel
    UMBELS = 98 # Dolden
    BOTTLES = 99 # Flaschen
    KNIFE_EDGES = 100 # Messerspitzen
    SMALL_BOWLS = 101 # Schälchen
    NOTE = 102 # Briefchen
    LATCH = 103 # Riegel
    POTS = 104 # Töpfe
    UNIT_CHOICES = [
        (KILOGRAM, 'kg'),
        (PIECES, 'Stück'),
        (GRAM, 'g'),
        (TABLESPOON, 'Esslöffel'),
        (TEASPOON, 'Teelöffel'),
        (MILILITER, 'ml'),
        (SOME, 'etwas'),
        (LITER, 'l'),
        (PACKS, 'Packungen'),
        (HAND_FULL, 'handvoll'),
        (STEM, 'Stängel'),
        (KNIFE_TIP, 'Msp.'),
        (BUNCH, 'Bund'),
        (PINCH, 'Prise'),
        (STICK, 'Stange'),
        (CAN, 'Dose'),
        (CANS, 'Dosen'),
        (STEMS, 'Stiele'),
        (SLICES, 'Scheiben'),
        (TWIGS, 'Zweige'),
        (TUBERS, 'Knollen'),
        (THICK, 'dick'),
        (SPLASHES, 'Spritzer'),
        (LEAVES, 'Blätter'),
        (CUBES, 'Würfel'),
        (TWIG, 'Zweig'),
        (PACK, 'Packung'),
        (PLATE, 'Platte'),
        (STICKS, 'Stangen'),
        (BALL, 'Ball'),
        (BOX, 'Kästchen'),
        (SHEETS, 'Blätter'),
        (PACKAGES, 'Päckchen'),
        (SLICE, 'Scheibe'),
        (GLASS, 'Glas'),
        (PINCHES, 'Prisen'),
        (BAG, 'Tüte'),
        (SMALL, 'kleine'),
        (SMALLER, 'kleiner'),
        (PANICLE, 'Rispe'),
        (HEAD, 'Kopf'),
        (PAIR, 'paar'),
        (BED, 'Beet'),
        (CLOVE, 'Zehe'),
        (PANICLES, 'Rispen'),
        (BALLS, 'Bälle'),
        (LEAVE, 'Blatt'),
        (STEM, 'Stiel'),
        (PODS, 'Schoten'),
        (FLAKES, 'Plättchen'),
        (CUP, 'Becher'),
        (GREAT, 'großer'),
        (CM, 'cm'),
        (HEADS, 'Köpfe'),
        (BOTTLE, 'Flasche'),
        (LONG, 'lange'),
        (YOUNG, 'junge'),
        (SACHETS, 'Tütchen'),
        (POUCH, 'Beutel'),
        (LACING, 'Schuss'),
        (MEDIUM_SIZED, 'mittelgroße'),
        (COOKING_BAG, 'Kochbeutel'),
        (LITTLE_TIN, 'Döschen'),
        (TUBER, 'Knolle'),
        (DROP, 'Tropfen'),
        (M, 'm'),
        (RING, 'Ring'),
        (CUPS, 'Becher'),
        (PACKAGE, 'Packet'),
        (DROPS, 'Tropfen'),
        (SHRUB, 'Staude'),
        (CLOVES, 'Zehen'),
        (FULL, 'voll'),
        (BEDS, 'Beete'),
        (ROLLS, 'Rollen'),
        (SMALLER, 'kleinerer'),
        (CL, 'cl'),
        (LEAN, 'schlanke'),
        (JARS, 'Gläser'),
        (STRIPES, 'Streifen'),
        (PORTION, 'Portion'),
        (MUG, 'Tasse'),
        (ROLL, 'Rolle'),
        (BLOCKS, 'Blöcke'),
        (SHRUBS, 'Stauden'),
        (PLATES, 'Platten'),
        (HERB_BOUQUET, 'Kräutersträußchen'),
        (SPIKES, 'Zacken'),
        (HERBAGE_BUNDLE, 'Kräuterbund'),
        (HANDS_FULL, 'Händevoll'),
        (BOWLS, 'Schalen'),
        (POTTY, 'Töpfchen'),
        (RINGS, 'Ringe'),
        (MOULDS, 'Förmchen'),
        (VIALS, 'Fläschchen'),
        (BAR, 'Tafel'),
        (UMBELS, 'Dolden'),
        (BOTTLES, 'Flaschen'),
        (KNIFE_EDGES, 'Messerspitzen'),
        (SMALL_BOWLS, 'Schälchen'),
        (NOTE, 'Briefchen'),
        (LATCH, 'Riegel'),
        (POTS, 'Töpfe'),
        (NO_UNIT, ''), 
    ]
    name = models.ForeignKey('IngredientName', on_delete=models.RESTRICT)
    amount = models.CharField(max_length=50, default='', null=True, blank=True)
    unit = models.PositiveSmallIntegerField(choices=UNIT_CHOICES, default=NO_UNIT)
    recipe = models.ForeignKey('Recipe', related_name='ingredients', on_delete=models.RESTRICT, null=True, blank=True, default=None)
    sub_category = models.CharField(max_length=100, null=True, blank=True)

class IngredientName(models.Model):
    name = models.CharField(max_length=140)

    def __str__(self):
        return self.name

class BarCode(models.Model):
    purchasing_item = models.ForeignKey('PurchasingItem', on_delete=models.RESTRICT)
    code = models.BigIntegerField(unique=True)

    def __str__(self):
        return str(self.code)