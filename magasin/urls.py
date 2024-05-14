from django.urls import path,include
from .views import CategoryAPIView,ProduitAPIView
from . import views

urlpatterns = [
    path('', views.index ,name='index'),
    path('mesProduit/', views.produit ,name='mesProduit'),
    path('majproduit/', views.majproduit ,name='majproduit'),
    path('catalogue/', views.catalogue ,name='cataloque'),
    path('commande/', views.Commandee ,name='commande'),
    path('MesCommande/', views.ListCmd ,name='ListCmd'),

    path('nouvFournisseur/',views.nouveauFournisseur,name='nouveauFour'),
    path('cmd/', views.ListCmd ,name='cmd'),
    path('register/',views.register, name = 'register'), 
    path('change-password/',views.change_password, name='change_password'),
    path('api/category/', CategoryAPIView.as_view()),
    path('api/produits/', ProduitAPIView.as_view())

]