from django.conf import settings
from django.core.management.base import BaseCommand
import pandas as pd
from map.models import Excavations

class Command(BaseCommand):
    help = 'Load data from .csv file to sqlite database'

    def handle(self, *args, **kwargs):
        data_file = settings.BASE_DIR / 'data' / 'zestawienie_zabytki_archeologiczne.csv'
        data = pd.read_csv(data_file, delimiter=';', on_bad_lines='warn')

        for row in data.iterrows():
            excavation = Excavations()

            excavation.INSPIRE_ID = row[1]['INSPIRE_ID']
            excavation.CHRONOLOGIA = row[1]['CHRONOLOGIA']
            excavation.FUNKCJA = row[1]['FUNKCJA']
            excavation.MIEJSCOWOSC = row[1]['MIEJSCOWOSC']
            excavation.LINK = row[1]['LINK']

            excavation.save()
