from django.db import models
from datetime import date


class Fournisseur(models.Model):
    nom = models.CharField(max_length=100)
    adresse = models.TextField()
    email = models.EmailField()
    telephone = models.CharField(max_length=8)
    def __str__(self):
        return self.nom
    
class Categorie (models.Model):
    TYPE_CHOICES=[
    ('Al','Alimentaire'), ('Mb','Meuble'),
    ('Sn','Sanitaire'), ('Vs','Vaisselle'),
    ('Vt','Vêtement'),('Jx','Jouets'),
    ('Lg','Linge de Maison'),('Bj','Bijoux'),('Dc','Décor')]
    name=models.CharField(max_length=50 ,choices=TYPE_CHOICES, default='Alimentaire')
    def __str__(self):
        return f"{self.name} "

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
    img=models.ImageField(blank=True)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, null=True)
    fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.libelle} - {self.description} - {self.prix} - {self.type}"

class ProduitNC(Produit):
    Duree_garantie = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.libelle} - Garantie: {self.Duree_garantie}"
    
class Commande(models.Model):
    dateCde = models.DateField(null=True, default=date.today)
    totalCde = models.DecimalField(max_digits=10, decimal_places=3,null=True)
    produits = models.ManyToManyField(Produit)

    def allProducts(self):
        ch=""
        for produit in self.produits.all():
            ch+=produit.__str__()
        return ch 
    def priceproduct(self):
        p=0
        for produit in self.produits.all() :
            p+=produit.prix
        self.totalCde=p
        self.save() 

    
    def __str__(self):
        return f"Commande du {self.dateCde} {self.allProducts()}"