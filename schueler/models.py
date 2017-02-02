from django.db import models
from django.utils import timezone

Lerngruppen_CHOICES = (
    ('Hydrix', 'Hydrix'),
    ('Panthera', 'Panthera'),
    ('Natrix', 'Natrix'),
    ('Orxgym', 'Orxgym'),
    ('Lupus', 'Lupus'),
)


class Schueler(models.Model):
    schuelerID = models.PositiveSmallIntegerField()
    vorname = models.CharField(max_length=15)
    name = models.CharField(max_length=15)
    geburtstag = models.DateField()
    Wohnort = models.CharField(max_length=15)
    Schulende = models.PositiveSmallIntegerField()
    Lerngruppe = models.CharField(choices=Lerngruppen_CHOICES, max_length=15)

    def publish(self):
        self.save()

    def __str__(self):
        return self.vorname

# Create your models here.
