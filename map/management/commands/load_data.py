from django.conf import settings
from django.core.management.base import BaseCommand
import pandas as pd
from map.models import Excavations

class Command(BaseCommand):
    help = 'Load csv'

    def handle(self, *args, **kwargs):

        # Connect to the database
        data_file = settings.BASE_DIR / 'data' / 'zestawienie_zabytki_archeologiczne.csv'
        data = pd.read_csv(data_file, delimiter=';', on_bad_lines='warn')

        for row in data.iterrows():
            excavation = Excavations()

            excavation.INSPIRE_ID = row[1][0]
            excavation.FORMA_OCHRONY = row[1][1]
            excavation.DOKLADNOSC_POLOZENIA = row[1][2]
            excavation.NAZWA = row[1][3]
            excavation.OBSZAR_AZP = row[1][4]
            excavation.NR_STANOWISKA_OBSZAR = row[1][5] if not pd.isna(row[1][5]) else 'brak'
            excavation.CHRONOLOGIA = row[1][6]
            excavation.FUNKCJA = row[1][7]
            excavation.WYKAZ_DOKUMENTOW = row[1][8]
            excavation.DATA_WPISU = row[1][9]
            excavation.WOJEWODZTWO = row[1][10]
            excavation.POWIAT = row[1][11]
            excavation.GMINA = row[1][12]
            excavation.MIEJSCOWOSC = row[1][13]
            excavation.LINK = row[1][14]

            excavation.save()