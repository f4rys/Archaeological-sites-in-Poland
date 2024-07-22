import glob
import os

import pandas as pd
from django.conf import settings
from django.core.management.base import BaseCommand

from map.models import Excavations


class Command(BaseCommand):
    help = 'Load data from .csv file to sqlite database'

    def handle(self, *args, **kwargs):
        data_dir = settings.BASE_DIR / 'data'
        pattern = f"{data_dir}/*.csv"
        prefix = "zestawienie-zabytki-archeologiczne"

        matching_files = glob.glob(pattern)

        data_file = None
        for file in matching_files:
            if file.startswith(os.path.join(data_dir, prefix)):
                data_file = file
                break

        if data_file:
            data = pd.read_csv(data_file, delimiter=';', on_bad_lines='warn')

            for row in data.iterrows():
                excavation = Excavations()

                excavation.INSPIRE_ID = row[1]['INSPIRE_ID']
                excavation.CHRONOLOGIA = row[1]['CHRONOLOGIA']
                excavation.FUNKCJA = row[1]['FUNKCJA']
                excavation.MIEJSCOWOSC = row[1]['MIEJSCOWOSC']
                excavation.LINK = row[1]['LINK']

                excavation.save()
        else:
            raise FileNotFoundError(f"No source file found in {data_dir}")
