

from django.db import models

class Tur(models.Model):
    nomi = models.CharField(max_length=100)

    def __str__(self):
        return self.nomi

class Gul(models.Model):
    nomi = models.CharField(max_length=100)
    tur = models.ForeignKey(Tur, related_name="gullar", on_delete=models.CASCADE)

    def __str__(self):
        return self.nomi



