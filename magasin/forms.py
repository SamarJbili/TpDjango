from django.forms import ModelForm
from django import forms
from .models import Produit,Commande,Fournisseur
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm as DjangoPasswordChangeForm
from django.contrib.auth.forms import UserCreationForm
class ProduitForm(ModelForm): 
    class Meta : 
        model = Produit 
        fields = "__all__" #pour tous les champs de la table
    #fields=['libelle','description'] #pour qulques champs
class CommandeForm(ModelForm):
    class Meta:
        model=Commande
        fields = ['produits']
        
class FournisseurForm(ModelForm):
    class Meta:
        model=Fournisseur
        fields="__all__"


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(label='Prénom')
    last_name = forms.CharField(label='Nom')
    email = forms.EmailField(label='Adresse e-mail')
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name' , 'email')



class PasswordChangeForm(DjangoPasswordChangeForm):

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
