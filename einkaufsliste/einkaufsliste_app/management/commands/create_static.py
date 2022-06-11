from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup, Doctype
import os
import shutil

class Command(BaseCommand):
    def add_arguments(self, parser):

        parser.add_argument(
                '--create',
                action='store_true',
                help='Create the correct path for the Static files',
            )

    def handle(self, *args, **options):

        if options['create']:
            # print(os.listdir('.././Frontend/nuxt-app/.output/public/_nuxt'))
            # delete all old files
            dir = './einkaufsliste_app/static/_nuxt'
            for f in os.listdir(dir):
                os.remove(os.path.join(dir, f))
            
            # same for templates
            dir = './einkaufsliste_app/templates'
            for f in os.listdir(dir):
                os.remove(os.path.join(dir, f))

            # copy new files
            source_folder = ".././Frontend/nuxt-app/.output/public/_nuxt"
            destination_folder = "./einkaufsliste_app/static/_nuxt"
            for file in os.listdir(source_folder):
                source = os.path.join(source_folder, file)
                destination = os.path.join(destination_folder, file)
                if os.path.isfile(source):
                    shutil.copy(source, destination)

            # same for templates
            source_folder = ".././Frontend/nuxt-app/.output/public"
            destination_folder = "./einkaufsliste_app/templates"
            for file in os.listdir(source_folder):
                source = os.path.join(source_folder, file)
                destination = os.path.join(destination_folder, file)
                if os.path.isfile(source):
                    shutil.copy(source, destination)

            files = [f for f in os.listdir('./einkaufsliste_app/templates')]
            for f in files:
                with open(os.path.join('./einkaufsliste_app/templates', f)) as file:
                    soup = BeautifulSoup(file, 'html.parser')
                links = soup.find_all('link')
                for link in links:
                    if link.has_attr('href'):
                        link['href'] = r"{% static '" + link['href'] + r"' %}"
                for script in soup.find_all('script'):
                    if script.has_attr('src'):
                        script['src'] = r"{% static '" + script['src'] + r"' %}"
                items = [item for item in soup.contents if isinstance(item, Doctype)]
                items[0].insert_before('{% load static %}\n')
                with open(os.path.join('./einkaufsliste_app/templates', f), "w") as file:
                    file.write(str(soup))
