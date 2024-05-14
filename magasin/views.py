from django.shortcuts import render,redirect,HttpResponseRedirect
from .models import Produit ,Fournisseur ,Commande
from .forms import ProduitForm,CommandeForm,FournisseurForm,UserCreationForm
from .forms import ProduitForm, FournisseurForm,UserRegistrationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
# Create your views here.

def catalogue(request):
    list=Produit.objects.all()
    return render(request,'magasin/vitrine.html',{'list':list})


def produit(request):
    products= Produit.objects.all()
    context={'products':products}    
    return render(request,'magasin/mesProduit.html',context)

def index (request):
    products= Produit.objects.all()
    context={'products':products}    
    return render(request,'magasin/index.html',context)

def majproduit(request):
    if request.method == "POST" : 
        form = ProduitForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('mesProduit')
    else :
        form = ProduitForm() 
    return render(request,'magasin/majProduits.html',{'form':form})

def Commandee(request):
    if request.method == "POST" : 
        form1 = CommandeForm(request.POST,request.FILES)
        if form1.is_valid():
            form1.save()
            return redirect('commande')
    else :
        form1 = CommandeForm() 
    return render(request, 'magasin/commande.html', {'form1': form1})



def nouveauFournisseur(request):
    if request.method == 'POST':
        form = FournisseurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('nouveauFour')
    else:
        form = FournisseurForm()
    
    # Récupérer tous les fournisseurs disponibles
    liste_des_fournisseurs = Fournisseur.objects.all()
    
    return render(request, 'magasin/Fournisseur.html', {'form': form, 'liste_des_fournisseurs': liste_des_fournisseurs})

from django.db.models import Sum

from decimal import Decimal

from decimal import Decimal

from decimal import Decimal
from django.db.models import Sum

def ListCmd(request):
    commandes = Commande.objects.all()
    total_commandes = Decimal(0)
    for commande in commandes:
        total_commandes += commande.produits.aggregate(total_price=Sum('prix'))['total_price'] or Decimal(0)
    context = {'commandes': commandes, 'total_commandes': total_commandes}
    return render(request, 'magasin/mesCommandes.html', context)

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f'Coucou {username}, Votre compte a été créé avec succès!')
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'magasin/registration/register.html', {'form': form})


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Met à jour la session de l'utilisateur pour éviter la déconnexion
            messages.success(request, 'Votre mot de passe a été changé avec succès!')
            return redirect('home')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'magasin/registration/change_password.html', {'form': form})

from rest_framework.views import APIView
from rest_framework.response import Response
from magasin.models import Categorie,Produit
from magasin.serializers import CategorySerializer,ProduitSerializer
from rest_framework import status

class CategoryAPIView(APIView):
    def get(self, *args, **kwargs):
        categories = Categorie.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

class ProduitAPIView(APIView):
    def get(self, *args, **kwargs):
        produits = Produit.objects.all()
        serializer = ProduitSerializer(produits, many=True)
        return Response(serializer.data)
    
from rest_framework import viewsets

class ProductViewset(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProduitSerializer
    def get_queryset(self):
        queryset = Produit.objects.filter()
        category_id = self.request.GET.get('category_id')
        if category_id:
            queryset = queryset.filter(categorie_id=category_id)
        return queryset
