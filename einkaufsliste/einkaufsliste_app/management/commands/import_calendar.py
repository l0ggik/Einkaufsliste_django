from django.core.management.base import BaseCommand
from einkaufsliste_app.models import WasteEvent
from ics import Calendar

class Command(BaseCommand):
    def add_arguments(self, parser):

        parser.add_argument(
                '--import',
                action='store_true',
                help='Import the waste calendar',
            )

    def handle(self, *args, **options):
        if options['import']:
            with open("./Abfuhrtermine.ics") as file:
                c = Calendar(file.read())
            events = list(c.timeline)
            for event in events:
                waste_event = WasteEvent(name=event.name, event_date=event.begin.date())
                waste_event.save()