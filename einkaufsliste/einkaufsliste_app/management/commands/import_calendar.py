from django.core.management.base import BaseCommand
from einkaufsliste_app.models import WasteEvent
from ics import Calendar
import requests

class Command(BaseCommand):
    def add_arguments(self, parser):

        parser.add_argument(
                '--import',
                action='store_true',
                help='Import the waste calendar',
            )

    def handle(self, *args, **options):
        if options['import']:
            response = requests.get('https://www.awsh.de/api_v2/collection_dates/1/ort/561/strasse/220/hausnummern/0/abfallarten/R02-B02-D02-P04/kalender.ics')
            c = Calendar(response.text)
            events = list(c.timeline)
            for event in events:
                waste_event = WasteEvent(name=event.name, event_date=event.begin.date())
                waste_event.save()