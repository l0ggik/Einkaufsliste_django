from genericpath import isfile
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
                if os.path.isfile(os.path.join(dir, f)):
                    os.remove(os.path.join(dir, f))
                elif os.path.isdir(os.path.join(dir, f)):
                    folder_path = os.path.join(dir, f)
                    for file in os.listdir(folder_path):
                       os.remove(os.path.join(folder_path, file))
                    os.rmdir(folder_path)

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
                elif file != '_nuxt' and os.path.isdir(os.path.join(source_folder, file)):
                    nested_source_folder = os.path.join(source_folder, file)
                    nested_destination_folder = os.path.join(destination_folder, file)
                    os.mkdir(nested_destination_folder)
                    for nested_file in os.listdir(nested_source_folder):
                        nested_source = os.path.join(nested_source_folder, nested_file)
                        nested_destination = os.path.join(nested_destination_folder, nested_file)
                        
                        if os.path.isfile(nested_source):
                            shutil.copy(nested_source, nested_destination)
                    
            

            root_folder = './einkaufsliste_app/templates'
            directories = [os.path.join(root_folder, dir) for dir in os.listdir(root_folder) if os.path.isdir(os.path.join(root_folder, dir))]
            files = [f for f in os.listdir(root_folder)]
            for f in files:
                if os.path.isfile(os.path.join(root_folder, f)):
                    with open(os.path.join(root_folder, f)) as file:
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
                    with open(os.path.join(root_folder, f), "w") as file:
                        file.write(str(soup))
            for directory in directories:
                files = [f for f in os.listdir(directory)]
                for f in files:
                    create_static_html(directory, f)

def create_static_html(folder, filename):
    if os.path.isfile(os.path.join(folder, filename)):
        with open(os.path.join(folder, filename)) as file:
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
        with open(os.path.join(folder, filename), "w") as file:
            file.write(str(soup))