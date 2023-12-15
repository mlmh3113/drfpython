from django.db import models
from .choices import animal_type

class Pet(models.Model):
    name = models.CharField(max_length=50, verbose_name='Name')
    birt_date = models.DateField(verbose_name='Birth date')
    animal_type = models.CharField(max_length=50, verbose_name='Animal type', choices=animal_type)
    owner = models.CharField(max_length=50, verbose_name='Owner')
    simtoms = models.TextField(verbose_name='Simtoms')

    class Meta:
        verbose_name = 'Pet'
        verbose_name_plural = 'Pets'
        ordering = ['name']

    def __str__(self):
        return self.name + ' - ' + self.animal_type + ' - ' + self.owner
