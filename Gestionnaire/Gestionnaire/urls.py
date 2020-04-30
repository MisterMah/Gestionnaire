"""Gestionnaire URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # Site Admin
    path('admin/', admin.site.urls),

    # home
    path('', views.home, name='home'),

    # gProduit
    path('gProduit/liste-des-produits', views.listProduits, name='listProduits'),
    path('gProduit/ajouter-un-produit', views.addProduits, name='addProduits'),
    path('gProduit/supprimer-un-produit', views.deleteProduits, name='deleteProduits'),
    path('gProduit/modifier-un-produit/<str:pk>', views.updateProduits, name='updateProduits'),
    path('gProduit/detail-produit/<str:pk>', views.detailProduits, name='detailProduits'),

    # gUtilisateurs
    path('gUtilisateur/liste-des-utilisateurs', views.listUtilisateurs, name='listUtilisateurs'),
    path('gUtilisateur/ajouter-un-utilisateur', views.addUtilisateurs, name='addUtilisateurs'),
    path('gUtilisateur/supprimer-un-utilisateur', views.deleteUtilisateurs, name='deleteUtilisateurs'),
    path('gUtilisateur/modifier-un-utilisateur/', views.updateUtilisateurs, name='updateUtilisateurs'),
    path('gUtilisateur/attribuer-des-permissions', views.permissionUtilisateurs, name='permissionUtilisateurs'),

    # gTicket
    path('gTicket/liste-des-tickets', views.listTickets, name='listTickets'),
    path('gTicket/ouvrir-un-ticket', views.addTickets, name='addTickets'),
    path('gTicket/supprimer-un-ticket', views.deleteTickets, name='deleteTickets'),
    path('gTicket/modifier-un-ticket/<str:pk>', views.updateTickets, name='updateTickets'),
    path('gTicket/detail-ticket/<str:pk>', views.detailTickets, name='detailTickets'),
    path('gTicket/gestion-etat-des-tickets', views.etatTickets, name='etatTickets'),
    path('gTicket/categorisation-des-tickets', views.categorizeTickets, name='categorizeTickets'),
    path('gTicket/detail-categorie/<str:pk>', views.detailCategorie, name='detailCategorie'),
    path('gTicket/assignation-support-delai-gravite-au-ticket', views.assignTickets, name='assignTickets'),

    # Signup
    path('accounts/signup/', views.signup, name="signup"),

    # Login
    path("login/", views.login_view, name = "login"),
    path("accounts/login/", views.login_view, name = "login"),

    # Logout
    path("logout/", views.logout_view, name = "logout_view"),
    path("accounts/logout/", views.logout_view, name = "logout_view"),

]
