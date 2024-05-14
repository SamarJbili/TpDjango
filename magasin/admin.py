from django.contrib import admin

# Register your models here.
from .models import Produit
from .models import Categorie
from .models import Fournisseur, ProduitNC,Commande

admin.site.register(Produit)
admin.site.register(Categorie)
admin.site.register(Fournisseur)
admin.site.register(ProduitNC)
admin.site.register(Commande)
