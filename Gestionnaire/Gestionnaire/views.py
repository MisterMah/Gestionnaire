from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout, get_user_model
from datetime import datetime
from pytz import timezone
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from .models import (
    Produit,
    Ticket,
    Categorie,
    Assignation,
)

# Variables
ROW_NUMBER_PER_PAGE = 15

# Create your views here.

#############
# Accueil
#############
@login_required
def home(request):

    return render(request, 'Gestionnaire/home.html', locals())


#############
# gProduits
#############
@login_required
def listProduits(request):
    context = {}
    query = ""
    produits = Produit.objects.all()
    all_produits = produits.count()

    if request.GET:
        query = request.GET.get('q', '')
        context['query'] = str(query)

    if query:
        queryset = []
        queries = query.split(" ")

        for q in queries:
            objects = Produit.objects.filter(
                Q(name__icontains=q) |
                Q(version__icontains=q) |
                Q(description__icontains=q)
                ).distinct()

            for object in objects:
                queryset.append(object)

        produits = list(set(queryset))
        number_produits = len(produits)
    else:
        number_produits = produits.count()

    # pagination
    page = request.GET.get('page', 1)
    produits_paginator = Paginator(produits, ROW_NUMBER_PER_PAGE)

    try:
        produits = produits_paginator.page(page)
    except PageNotAnInteger:
        produits = produits_paginator.page(ROW_NUMBER_PER_PAGE)
    except EmptyPage:
        produits = produits_paginator.page(produits_paginator.num_pages)

    context[produits] = produits
    num = len(produits)

    return render(request, 'Gestionnaire/listProduits.html', locals())

@login_required
def addProduits(request):
    created = None
    produits = Produit.objects.all()
    number_produits = produits.count()

    if request.method == 'POST':
        name = request.POST.get("name")
        version = request.POST.get("version")
        description = request.POST.get("description")

        now = datetime.now()
        dateCreation = now

        try:
            s, created = Produit.objects.get_or_create(name=name, version=version, description=description, dateCreation=dateCreation)
        except IntegrityError as error:
            error = "Ce produit '{}' existe déjà !!!".format(name)
            return render(request, 'Gestionnaire/addProduits.html', locals())

        if created:
            success = "Enregistré avec succès !!!"
        else:
            error = "Ce produit '{}' existe déjà !!!".format(name)

    return render(request, 'Gestionnaire/addProduits.html', locals())

@login_required
def deleteProduits(request):

    return render(request, 'Gestionnaire/deleteProduits.html', locals())

@login_required
def updateProduits(request, pk):

    return render(request, 'Gestionnaire/updateProduits.html', locals())

@login_required
def detailProduits(request, pk):

    return render(request, 'Gestionnaire/detailProduits.html', locals())


#################
# gUtilisateurs
#################
@login_required
def listUtilisateurs(request):
    # context = {}
    # query = ""
    # utilisateurs = User.objects.all()
    # all_utilisateurs = utilisateurs.count()
    #
    # if request.GET:
    #     query = request.GET.get('q', '')
    #     context['query'] = str(query)
    #
    # if query:
    #     queryset = []
    #     queries = query.split(" ")
    #
    #     for q in queries:
    #         objects = User.objects.filter(
    #             Q(username__icontains=q) |
    #             Q(first_name__icontains=q) |
    #             Q(last_name__icontains=q) |
    #             Q(group__icontains=q)
    #             ).distinct()
    #
    #         for object in objects:
    #             queryset.append(object)
    #
    #     utilisateurs = list(set(queryset))
    #     number_utilisateurs = len(utilisateurs)
    # else:
    #     number_utilisateurs = utilisateurs.count()
    #
    # # pagination
    # page = request.GET.get('page', 1)
    # utilisateurs_paginator = Paginator(utilisateurs, ROW_NUMBER_PER_PAGE)
    #
    # try:
    #     utilisateurs = utilisateurs_paginator.page(page)
    # except PageNotAnInteger:
    #     utilisateurs = utilisateurs_paginator.page(ROW_NUMBER_PER_PAGE)
    # except EmptyPage:
    #     utilisateurs = utilisateurs_paginator.page(utilisateurs_paginator.num_pages)
    #
    # context[utilisateurs] = utilisateurs
    # num = len(utilisateurs)

    return render(request, 'Gestionnaire/listUtilisateurs.html', locals())

@login_required
def addUtilisateurs(request):

    return render(request, 'Gestionnaire/addUtilisateurs.html', locals())

@login_required
def deleteUtilisateurs(request):

    return render(request, 'Gestionnaire/deleteUtilisateurs.html', locals())

@login_required
def updateUtilisateurs(request):

    return render(request, 'Gestionnaire/updateUtilisateurs.html', locals())

@login_required
def permissionUtilisateurs(request):

    return render(request, 'Gestionnaire/permissionUtilisateurs.html', locals())


##############
# gTickets
##############
@login_required
def listTickets(request):
    context = {}
    query = ""
    tickets = Ticket.objects.all()
    all_tickets = tickets.count()

    if request.GET:
        query = request.GET.get('q', '')
        context['query'] = str(query)

    if query:
        queryset = []
        queries = query.split(" ")

        for q in queries:
            objects = Ticket.objects.filter(
                Q(name__icontains=q) |
                Q(ip_address__icontains=q) |
                Q(os_type__os_name__icontains=q) |
                Q(owner__name__icontains=q)
                ).distinct()

            for object in objects:
                queryset.append(object)

        tickets = list(set(queryset))
        number_tickets = len(tickets)
    else:
        number_tickets = tickets.count()

    # pagination
    page = request.GET.get('page', 1)
    tickets_paginator = Paginator(tickets, ROW_NUMBER_PER_PAGE)

    try:
        tickets = tickets_paginator.page(page)
    except PageNotAnInteger:
        tickets = tickets_paginator.page(ROW_NUMBER_PER_PAGE)
    except EmptyPage:
        tickets = tickets_paginator.page(tickets_paginator.num_pages)

    context[tickets] = tickets
    num = len(tickets)

    return render(request, 'Gestionnaire/listTickets.html', locals())

@login_required
def addTickets(request):
    created = None
    produits = Produit.objects.all()
    users = User.objects.all()
    tickets = Ticket.objects.all()
    number_tickets = tickets.count()

    if request.method == 'POST':
        titre = request.POST.get("titre")
        produit_pk = request.POST.get("produit")
        description = request.POST.get("description")
        solution = "Aucun"

        produit = produits.get(pk=produit_pk)
        initiateur = users.get(username=request.user.username)

        now = datetime.now()
        dateOuverture = now

        try:
            s, created = Ticket.objects.get_or_create(titre=titre, produit=produit, initiateur=initiateur, dateOuverture=dateOuverture, description=description, solution=solution)
        except IntegrityError as error:
            error = "Ce ticket '{}' existe déjà !!!".format(titre)
            return render(request, 'Gestionnaire/addTickets.html', locals())

        if created:
            success = "Enregistré avec succès !!!"
        else:
            error = "Ce ticket '{}' existe déjà !!!".format(titre)

    return render(request, 'Gestionnaire/addTickets.html', locals())

@login_required
def deleteTickets(request):

    return render(request, 'Gestionnaire/deleteTickets.html', locals())

@login_required
def updateTickets(request, pk):

    return render(request, 'Gestionnaire/updateTickets.html', locals())

@login_required
def detailTickets(request, pk):
    ticket = Ticket.objects.get(pk=pk)

    return render(request, 'Gestionnaire/detailTickets.html', locals())

@login_required
def detailCategorie(request, pk):
    categorie = Categorie.objects.get(pk=pk)

    return render(request, 'Gestionnaire/detailCategorie.html', locals())

@login_required
def categorizeTickets(request):
    context = {}
    query = ""
    categories = Categorie.objects.all()
    tickets_set = Ticket.objects.all()
    supports_set = User.objects.all()

    if request.GET:
        query = request.GET.get('q', '')
        context['query'] = str(query)

    if query:
        queryset = []
        queries = query.split(" ")

        for q in queries:
            objects = Categorie.objects.filter(
                Q(name__icontains=q) |
                Q(description__icontains=q)
            ).distinct()

            for object in objects:
                queryset.append(object)

        categories = list(set(queryset))
        number_categories = len(categories)
    else:
        number_categories = categories.count()


    # pagination
    page = request.GET.get('page', 1)
    categories_paginator = Paginator(categories, ROW_NUMBER_PER_PAGE)

    try:
        categories = categories_paginator.page(page)
    except PageNotAnInteger:
        categories = categories_paginator.page(ROW_NUMBER_PER_PAGE)
    except EmptyPage:
        categories = categories_paginator.page(categories_paginator.num_pages)

    context[categories] = categories
    num = len(categories)

    # Pour ajouter une categories
    created = None
    categories = Categorie.objects.all()

    if request.method == 'POST':
        name = request.POST.get("name")

        tickets = [] # stocke les primary_key (pk)
        supports = [] # stocke les primary_key (pk)

        description = request.POST.get("description")

        now = datetime.now()
        date = now

        try:
            s, created = Categorie.objects.get_or_create(name=name, tickets=tickets, supports=supports, description=description, date=date)
        except IntegrityError as error:
            error = "Cette catégorie '{}' existe déjà !!!".format(name)
            return render(request, 'Gestionnaire/categorizeTickets.html', locals())

        if created:
            success = "Enregistrée avec succès !!!"
        else:
            error = "Cette catégorie '{}' existe déjà !!!".format(name)

    return render(request, 'Gestionnaire/categorizeTickets.html', locals())

@login_required
def assignTickets(request):
    context = {}
    query = ""
    assignations = Assignation.objects.all()
    all_assignations = assignations.count()

    if request.GET:
        query = request.GET.get('q', '')
        context['query'] = str(query)

    if query:
        queryset = []
        queries = query.split(" ")

        for q in queries:
            objects = Assignation.objects.filter(
                Q(ticket__titre__icontains=q) |
                Q(ticket__produit__name__icontains=q) |
                Q(support__username__icontains=q)
            ).distinct()

            for object in objects:
                queryset.append(object)

        assignations = list(set(queryset))
        number_assignations = len(assignations)
    else:
        number_assignations = assignations.count()

    # pagination
    page = request.GET.get('page', 1)
    assignations_paginator = Paginator(assignations, ROW_NUMBER_PER_PAGE)

    try:
        assignations = assignations_paginator.page(page)
    except PageNotAnInteger:
        assignations = assignations_paginator.page(ROW_NUMBER_PER_PAGE)
    except EmptyPage:
        assignations = assignations_paginator.page(assignations_paginator.num_pages)

    context[assignations] = assignations
    num = len(assignations)

    # Pour ajouter une categories
    created = None
    assignations = Assignation.objects.all()
    categories = Categorie.objects.all()
    tickets = Ticket.objects.all()
    supports = User.objects.all() # Filtrer les utilisateurs avec le role "SUPPORT" après

    if request.method == 'POST':
        name = request.POST.get("categorie")
        ticket_pk = request.POST.get("ticket")
        support_pk = request.POST.get("support")
        gravite = request.POST.get("gravite")
        etat = request.POST.get("etat")
        delai = request.POST.get("delai")

        # recuperation des objets à partir de leurs pk
        categorie = categories.get(name=name)
        ticket = tickets.get(pk=ticket_pk)
        support = supports.get(pk=support_pk)

        # Mise à jour des colonnes tickets et supports du Modèle Categorie
        categorie.tickets.append(ticket) # stocke les primary_key (pk)
        categorie.supports.append(support) # stocke les primary_key (pk)
        categorie.save()

        now = datetime.now()
        dateAssignation = now

        try:
            s, created = Assignation.objects.get_or_create(categorie=categorie, ticket=ticket, support=support, gravite=gravite, etat=etat, delai=delai, dateAssignation=dateAssignation)
        except IntegrityError as error:
            error = "Cette assignation existe déjà !!!"
            return render(request, 'Gestionnaire/assignTickets.html', locals())

        if created:
            success = "Enregistrée avec succès !!!"
        else:
            error = "Cette assignation existe déjà !!!"

    return render(request, 'Gestionnaire/assignTickets.html', locals())

@login_required
def etatTickets(request):

    return render(request, 'Gestionnaire/etatTickets.html', locals())


def signup(request):

    return render(request, 'Gestionnaire/signup.html', locals())


# Login
def login_view(request):
    try:
        if request.session['user_id']:
            return redirect(home)
    except KeyError:
        pass

    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username = username, password = password)
        login(request, user)
        request.session['user_id'] = user.pk
        return redirect(home)

    return render(request, "Gestionnaire/login.html", locals())


# logout
@login_required
def logout_view(request):
    try:
        del request.session['user_id']
    except KeyError:
        pass

    logout(request)
    return redirect(login_view)
