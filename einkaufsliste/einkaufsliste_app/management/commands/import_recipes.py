from os import listdir
from os.path import isfile, join
import re
import sys
from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError
from bs4 import BeautifulSoup

from einkaufsliste_app.models import Ingredient, IngredientName, Recipe, Category


class Command(BaseCommand):
    def add_arguments(self, parser):

        parser.add_argument(
            '--import_main_dishes',
            action='store_true',
            help='Import recipes',
        )
        parser.add_argument(
            '--import_desserts',
            action='store_true',
            help='Import dessert recipes',
        )
        parser.add_argument(
            '--import_starters',
            action='store_true',
            help='Import starter recipes',
        )
        parser.add_argument(
            '--import_main_dishes_categories',
            action='store_true',
            help='Import recipes categories',
        )
        parser.add_argument(
            '--delete',
            action='store_true',
            help='Delete all Recipes and related stuff'
        )

    def handle(self, *args, **options):
        if options['import_main_dishes']:
            base_path = '/home/arne/Python-Projekte/Einkaufsliste_django/einkaufsliste/html/hauptspeisen/rezepte/'
            recipe_file_paths = [file for file in listdir(base_path) if isfile(join(base_path, file))]
            for counter, recipe_file_path in enumerate(recipe_file_paths[4020:], 4020):
                print(f'Lese Rezept Nummer {counter} ein')
                recipe_number = int(recipe_file_path.split('.')[0].split('-')[-1])
                with open(join(base_path, recipe_file_path), 'r') as recipe_file:
                    soup = BeautifulSoup(recipe_file, 'html.parser')
                headline = soup.find('h1', class_='headline')
                try:
                    title = headline.find('span', class_='headline__title')
                except AttributeError:
                    print(recipe_file_path)
                    continue
                    # sys.exit(0)
                preparation_div = soup.find('div', class_='recipe-preparation')
                try:
                    preparation_items_list = preparation_div.find('ol', class_='recipe-preparation__list')
                except AttributeError:
                    print(recipe_file_path)
                    continue
                preparation_items = preparation_items_list.find_all('li', class_='recipe-preparation__item')
                new_tag = soup.new_tag('p')
                for count, preparation_item in enumerate(preparation_items, 1):
                    new_tag.append(f'{str(count)}. {preparation_item.get_text().strip()}\n')
                ingredients_div = soup.find('div', class_='recipe-ingredients')
                ingredients_objects = []
                recipe_object = Recipe.objects.create(name=title.get_text().strip(), preparation=str(new_tag), number=recipe_number)
                # recipe_object = ''
                if ingredients_div.find('h3', class_='recipe-ingredients__subtitle'):
                    for subtitle in ingredients_div.find_all('h3', class_='recipe-ingredients__subtitle'):
                        ingredients_list = subtitle.find_next_sibling('ul', class_='recipe-ingredients__list')
                        ingredients_items = ingredients_list.find_all('li', class_='recipe-ingredients__item')
                        for ingredients_item in ingredients_items:
                            ingredients_objects.append(extract_ingredient(ingredients_item=ingredients_item, recipe_object=recipe_object, subtitle=subtitle.get_text()))
                else: 
                    ingredients_list = ingredients_div.find('ul', class_='recipe-ingredients__list')
                    ingredients_items = ingredients_list.find_all('li', class_='recipe-ingredients__item')
                    for ingredients_item in ingredients_items:
                        ingredients_objects.append(extract_ingredient(ingredients_item=ingredients_item, recipe_object=recipe_object))
                Ingredient.objects.bulk_create(ingredients_objects)
        
        if options['import_desserts']:
            base_path = '/home/arne/Python-Projekte/Einkaufsliste_django/einkaufsliste/html/dessert/rezepte/'
            recipe_file_paths = [file for file in listdir(base_path) if isfile(join(base_path, file))]
            for counter, recipe_file_path in enumerate(recipe_file_paths):
                print(f'Lese Rezept Nummer {counter} ein')
                recipe_number = int(recipe_file_path.split('.')[0].split('-')[-1])
                with open(join(base_path, recipe_file_path), 'r') as recipe_file:
                    soup = BeautifulSoup(recipe_file, 'html.parser')
                headline = soup.find('h1', class_='headline')
                try:
                    title = headline.find('span', class_='headline__title')
                except AttributeError:
                    print(recipe_file_path)
                    continue
                    # sys.exit(0)
                preparation_div = soup.find('div', class_='recipe-preparation')
                try:
                    preparation_items_list = preparation_div.find('ol', class_='recipe-preparation__list')
                except AttributeError:
                    print(recipe_file_path)
                    continue
                preparation_items = preparation_items_list.find_all('li', class_='recipe-preparation__item')
                new_tag = soup.new_tag('p')
                for count, preparation_item in enumerate(preparation_items, 1):
                    new_tag.append(f'{str(count)}. {preparation_item.get_text().strip()}\n')
                try:
                    recipe_object = Recipe.objects.create(name=title.get_text().strip(), preparation=str(new_tag), number=recipe_number)
                except IntegrityError:
                    print("Rezept bereits in Datenbank:", title)
                    continue
                    # sys.exit(0)
                # recipe_object = ''
                ingredients_objects = []
                ingredients_div = soup.find('div', class_='recipe-ingredients')
                if ingredients_div.find('h3', class_='recipe-ingredients__subtitle'):
                    for subtitle in ingredients_div.find_all('h3', class_='recipe-ingredients__subtitle'):
                        ingredients_list = subtitle.find_next_sibling('ul', class_='recipe-ingredients__list')
                        ingredients_items = ingredients_list.find_all('li', class_='recipe-ingredients__item')
                        for ingredients_item in ingredients_items:
                            ingredients_objects.append(extract_ingredient(ingredients_item=ingredients_item, recipe_object=recipe_object, subtitle=subtitle.get_text()))
                else: 
                    ingredients_list = ingredients_div.find('ul', class_='recipe-ingredients__list')
                    ingredients_items = ingredients_list.find_all('li', class_='recipe-ingredients__item')
                    for ingredients_item in ingredients_items:
                        ingredients_objects.append(extract_ingredient(ingredients_item=ingredients_item, recipe_object=recipe_object))
                Ingredient.objects.bulk_create(ingredients_objects)
                    
        if options['import_starters']:
            KNOWN_INGREDIENTS = []
            base_path = '/home/arne/Python-Projekte/Einkaufsliste_django/einkaufsliste/html/vorspeisen/rezepte/'
            recipe_file_paths = [file for file in listdir(base_path) if isfile(join(base_path, file))]
            for counter, recipe_file_path in enumerate(recipe_file_paths):
                print(f'Lese Rezept Nummer {counter} ein')
                recipe_number = int(recipe_file_path.split('.')[0].split('-')[-1])
                with open(join(base_path, recipe_file_path), 'r') as recipe_file:
                    soup = BeautifulSoup(recipe_file, 'html.parser')
                headline = soup.find('h1', class_='headline')
                try:
                    title = headline.find('span', class_='headline__title')
                except AttributeError:
                    print(recipe_file_path)
                    continue
                    # sys.exit(0)
                preparation_div = soup.find('div', class_='recipe-preparation')
                try:
                    preparation_items_list = preparation_div.find('ol', class_='recipe-preparation__list')
                except AttributeError:
                    print(recipe_file_path)
                    continue
                preparation_items = preparation_items_list.find_all('li', class_='recipe-preparation__item')
                new_tag = soup.new_tag('p')
                for count, preparation_item in enumerate(preparation_items, 1):
                    new_tag.append(f'{str(count)}. {preparation_item.get_text().strip()}\n')
                try:
                    recipe_object = Recipe.objects.create(name=title.get_text().strip(), preparation=str(new_tag), number=recipe_number)
                except IntegrityError:
                    print("Rezept bereits in Datenbank:", title)
                    continue
                    # sys.exit(0)
                ingredients_objects = []
                ingredients_div = soup.find('div', class_='recipe-ingredients')
                if ingredients_div.find('h3', class_='recipe-ingredients__subtitle'):
                    for subtitle in ingredients_div.find_all('h3', class_='recipe-ingredients__subtitle'):
                        ingredients_list = subtitle.find_next_sibling('ul', class_='recipe-ingredients__list')
                        ingredients_items = ingredients_list.find_all('li', class_='recipe-ingredients__item')
                        for ingredients_item in ingredients_items:
                            ingredients_objects.append(extract_ingredient(ingredients_item=ingredients_item, recipe_object=recipe_object, subtitle=subtitle.get_text()))
                else: 
                    ingredients_list = ingredients_div.find('ul', class_='recipe-ingredients__list')
                    ingredients_items = ingredients_list.find_all('li', class_='recipe-ingredients__item')
                    for ingredients_item in ingredients_items:
                        ingredients_objects.append(extract_ingredient(ingredients_item=ingredients_item, recipe_object=recipe_object))
                Ingredient.objects.bulk_create(ingredients_objects)
                    
        if options ['import_main_dishes_categories']:
            base_path = '/home/arne/Python-Projekte/Einkaufsliste_django/einkaufsliste/html/hauptspeisen/rezepte/'
            recipe_file_paths = [file for file in listdir(base_path) if isfile(join(base_path, file))]
            for counter, recipe_file_path in enumerate(recipe_file_paths):
            # for recipe_file_path in recipe_file_paths[0:6]:
                print(f'Lese Rezept Nummer {counter} ein')
                with open(join(base_path, recipe_file_path), 'r') as recipe_file:
                    soup = BeautifulSoup(recipe_file, 'html.parser')
                recipe_number = int(recipe_file_path.split('.')[0].split('-')[-1])
                headline = soup.find('h1', class_='headline')
                try:
                    title = headline.find('span', class_='headline__title')
                except AttributeError:
                    continue
                try:
                    recipe_object = Recipe.objects.get(number=recipe_number)
                # except (Recipe.DoesNotExist, Recipe.MultipleObjectsReturned):
                except Recipe.DoesNotExist:
                    # print(title)
                    continue
                recipe_categries_div = soup.find('div', class_='recipe-categories')
                try:
                    recipe_categories_list = recipe_categries_div.find('ul', class_='recipe-categories__list')
                except AttributeError:
                    continue
                recipe_categories_items = recipe_categories_list.find_all('li', class_='recipe-categories__item')
                recipe_categories_objects = []
                for recipe_category in recipe_categories_items:
                    if recipe_category.find('a'):
                        category_name = recipe_category.find('a').get_text()
                    elif recipe_category.find('span'):
                        category_name = recipe_category.find('span').get_text()
                    else:
                        print(f"Rezept {title} hat komische Kategorien")
                    recipe_category_object, created = Category.objects.get_or_create(name=category_name)
                    recipe_categories_objects.append(recipe_category_object)
                for category_object in recipe_categories_objects:
                    recipe_object.categories.add(category_object)
                recipe_object.save()
        if options ['delete']:
            Ingredient.objects.all().delete()
            Category.objects.all().delete()
            Recipe.objects.all().delete()

def extract_ingredient(ingredients_item, recipe_object, subtitle=None):
    UNITS = {
        'kg': 1,
        'kgR': 1, 
        'Stück': 2,
        'Stücke': 2,
        'STück': 2,
        'Stückq': 2,
        'g': 3,
        'ge': 3,
        'G': 3,
        'h': 3,
        'EL': 4,
        'El': 4,
        'Esslöffel': 4,
        'ELK': 4,
        'E': 4,
        'TL': 5,
        'Tl': 5, 
        'Teelöffel': 5,
        'Löffel': 5,
        'TLf': 5,
        'LTL': 5,
        'TKL': 5,
        'TK': 5,
        'ml': 6,
        'ML': 6,
        'einige': 8, 
        'l': 9,
        'L': 9,
        'Liter': 9,
        'kl': 9,
        'Packungen': 10, 
        'Handvoll': 11,
        'handvoll': 11,
        'Handvol': 11,
        'Stängel': 12, 
        'Msp.': 13,
        'Messerspitze': 13,
        'Msp,': 13,
        'Msp': 13,
        'Bund': 14,
        'Budn': 14,
        'BUnd': 14,
        'Vund': 14, 
        'Prise': 15,
        'prise': 15,
        'Priise': 15, 
        'Stange': 16,
        'Stang': 16,
        'Dose': 17, 
        'Dosen': 18, 
        'Stiele': 19, 
        'Scheiben': 20, 
        'Zweige': 21,
        'zweige': 21,
        'Knollen': 22,
        'dicke': 23,
        'Spritzer': 24,
        'Blätter': 25,
        'Würfel': 26,
        'Zweig': 27,
        'Zwieg': 27,
        'Pck': 28,
        'Pck.': 28,
        'Packung': 28,
        'Pk.': 28,
        'Platte': 29,
        'Stangen': 30,
        'STangen': 30,
        'Kugel': 31,
        'Kästchen': 32,
        'Bögen': 33,
        'Päckchen': 34,
        'Scheibe': 35,
        'Scheib': 35,
        'Glas': 36,
        'Prisen': 37,
        'Tüte': 38,
        'kleine': 39,
        'kleiner': 40,
        'Rispe': 41,
        'Kopf': 42,
        'paar': 43,
        'Paar': 43,
        'Beet': 44,
        'beet': 44,
        'Zehe': 45,
        'Rispen': 46,
        'Kugeln': 47,
        'Blatt': 48,
        'Bogen': 48,
        'Stiel': 49,
        'Schoten': 50,
        'Blättchen': 51,
        'Becher': 52,
        'große': 53,
        'cm': 54,
        'Köpfe': 55,
        'Flasche': 56,
        'lange': 57,
        'junge': 58,
        'Tütchen': 59,
        'Beutel': 60,
        'Schuss': 61,
        'mittelgroße': 62,
        'Kochbeutel': 63,
        'Döschen': 64,
        'Knolle': 65,
        'Tropfen': 66,
        'm': 67,
        'Ring': 68,
        'Tassen': 69,
        'Paket': 70,
        'Tropfen': 71,
        'Staude': 72,
        'Zehen': 73,
        'voll': 74,
        'Beete': 75,
        'Rollen': 76,
        'kleinerer': 77,
        'cl': 78,
        'schlanke': 79,
        'Gläser': 80,
        'Streifen': 81,
        'Portion': 82,
        'Tasse': 83,
        'Rolle': 84,
        'Blöcke': 85,
        'Stauden': 86,
        'Platten': 87,
        'Kräutersträußchen': 88,
        'Zacken': 89,
        'Kräuterbund': 90,
        'Händevoll': 91,
        'Schalen': 92,
        'Töpfchen': 93,
        'Ringe': 94,
        'Förmchen': 95,
        'Frömchen': 95,
        'Fläschchen': 96,
        'Tafel': 97,
        'Dolden': 98,
        'Flaschen': 99,
        'Messerspitzen': 100,
        'Schälchen': 101,
        'Briefchen': 102,
        'Riegel': 103,
        'Töpfe': 104,
    }
    KNOWN_TWO_PART_INGREDIENTS = ['5 - 6', '1 - 2', '2 - 3', '3 - 4', '4 - 5', '4 - 6', '3 - 5', '5- 10', '6 - 8', '6 - 7', '2- 3', '6- 8', '6 - 12', '8 - 10', '8 - 12', '9 - 10', '10 - 12', '8- 16', '10 - 14', '15 - 20', '16 - 20', '1- 2', 'ca. 1/4', 'ca. 4', 'ca. 5', 'ca. 9', 'ca. 10', 'ca. 12', 'ca. 40', 'ca. 15', 'ca. 20', 'ca. 30', 'ca. 35', 'ca. 45', 'ca. 70', '1 1/2', '2 1/2', 'je 1', 'je 2', 'je 3', 'je 4', 'je 2-3', 'je 5-10', 'je 10', 'je 1/2', 'je 150', 'ca. 6', 'ca. ⅓', '4 oder 8', 'evtl. 1', '1 ½', 'Saft und abgeriebene Schale von 1/2', 'Saft von 1/2', '3 gestr. EL (ca. 30 g)', 'Saft von', 'Saft von 1', '1 großes', '2 rote', '1 rote', '1 großes', '1/2 -2', '2 grüne', 'ca. 8', 'je 8', 'ca. 500', '4 große dünne', '1 kleines', '2 halbe', '100 g Allgäuer', '1 Schalotte', '1 Ei', '1 Eigelb', '2 ½ ½', '1 Dose (400 ml)', '20-24 klein', '1 Viertel', '2-3 große, saftige', 'frisch geriebene', '1 mittelgroßer', '1 dünner', '4 dicke Beinscheiben', '2 schmale', '20-30 Kohlrabiblätter', '2 Packungen (ca. 14 Scheiben)', '1 f', '1 M', '2 M', '3 M', '4 M', '5 M', '4 Größe M', '6 M', '7 M', '3 Größe M', '2 Größe M', 'evtl. etwas', '1 doppelter', '1 kleinere', 'Schale von 1', 'zum Bestäuben', 'ca. 20 Ø 70 mm', 'ca 16-20 blühende', '30 weiße', '2 Eier', '150 kalte', '60 Zucker', 'abgeriebene Schale', 'Mark von 1', '½ - 1', '2 Öl', '1/2 - 2', '2 Msp. Zimtpulver', '1 größere', '2 k', '2 Minze', 'ggf. etwas', 'Nach Belieben', '1 Knoblauchzehe', '1 Glas (400 ml)', '350 g gemahlene', '1 Rezept', 'evtl. 12', '1 Tüte (10 g)', '2/3 Rezept', '1 Rezept', 'abgeriebene Schale von 1', 'Schale von 1/2', 'ausgepresster Saft von 1/2', '1 grüne']
    ingredient_unit = 7 # 7 = No Unit
    ingredient_amount = re.sub(' +', ' ', ingredients_item.find('span', class_='recipe-ingredients__amount').get_text().strip().replace('\n', ''))
    split = ingredient_amount.split(' ')
    if len(split) > 2:
        if ingredient_amount in KNOWN_TWO_PART_INGREDIENTS:
            pass
        else:
            ingredient_unit = split[-1]
            if ingredient_unit in UNITS.keys():
                ingredient_unit = UNITS[ingredient_unit]
            else:
                print("Unbekannte Einheit gefunden:", ingredient_unit)
                print("Gesamte Zutat:", ingredient_amount)
            ingredient_amount = ' '.join(split[0:-1])
    elif len(split) > 1:
        if ingredient_amount in KNOWN_TWO_PART_INGREDIENTS:
            pass
        else:
            ingredient_unit = split[1]
            if ingredient_unit in UNITS.keys():
                ingredient_unit = UNITS[ingredient_unit]
            else:
                print("Unbekannte Einheit gefunden:", ingredient_unit)
                print("Gesamte Zutat:", ingredient_amount)
            ingredient_amount = split[0]
    elif ingredient_amount in UNITS.keys():
        ingredient_unit = UNITS[ingredient_amount]
        ingredient_amount = None
    ingredient_text = ingredients_item.find('span', class_='recipe-ingredients__text').get_text().strip()
    ingredient_name_object, created = IngredientName.objects.get_or_create(name=ingredient_text)
    return Ingredient(
        name=ingredient_name_object,
        amount = ingredient_amount,
        unit = ingredient_unit,
        recipe = recipe_object,
        sub_category = subtitle
    )
