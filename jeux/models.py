from django.db import models

# Create your models here.

class Produit(models.Model):
    TYPE_CHOICES = [
        ('em', 'emballé'),
        ('fr', 'Frais'),
        ('cs', 'Conserve')
    ]

    libelle = models.CharField(max_length=100)
    description = models.TextField(default='Non définie')
    prix = models.DecimalField(max_digits=10, decimal_places=3)
    type = models.CharField(max_length=2, choices=TYPE_CHOICES, default='em')

    def __str__(self):
        return f"{self.libelle} - {self.description} - {self.prix} - {self.type}"
