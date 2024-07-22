from django.db import models

class Excavations(models.Model):
    INSPIRE_ID = models.TextField(max_length=255)
    CHRONOLOGIA = models.TextField(max_length=255)
    FUNKCJA = models.TextField(max_length=255)
    MIEJSCOWOSC = models.TextField(max_length=255)
    LINK = models.TextField(max_length=255)

    objects = models.Manager()
