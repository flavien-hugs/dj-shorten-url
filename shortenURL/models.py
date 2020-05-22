# shortenURL/models.py

import random
import string
from django.db import models
from django.urls import reverse


class Shorten(models.Model):
    url = models.URLField('URL à réduire', unique=True)
    code = models.CharField(max_length=6, unique=True)
    date = models.DateField("Date d'enregistrement", auto_now_add=True)
    nb_acces = models.IntegerField('Nombre de vues', default=0)

    def __str__(self):
        return "[{0}] {1}".format(self.code, self.url)

    # Surchage de la methode save() pour generer automatiquement
    # le code de l'URl
    def save(self, *args, **kwargs):
        if self.pk is None:
            self.generate(6)
        super(Shorten, self).save(*args, **kwargs)

    def generate(self, nb_carac):
        carac = string.ascii_letters + string.ascii_uppercase + string.digits
        random_carac = [random.choice(carac) for _ in range(nb_carac)]
        self.code = ''.join(random_carac)


    class Meta:
        verbose_name = "Raccourcisseur d'URL"
        verbose_name_plural = "Raccourcisseurs d'URL"
