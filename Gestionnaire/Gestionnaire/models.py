from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from picklefield.fields import PickledObjectField # for dictField

# Create your models here.

# class Utilisateur(models.Model):
#     first_name = models.CharField('First Name', max_length=50)
#     last_name = models.CharField('Last Name', max_length=50)
#     username = models.CharField('Username', primary_key=True, max_length=50)
#     password = models.CharField('Password', max_length=50)
#     email = models.CharField('Email', max_length=50)
#     number = models.CharField('Number', max_length=50)
#     role = models.CharField('Role', max_length=50)
#
#     class Meta:
#         ordering = ["username",]
#
#     def __str__(self):
#         return "{}".format(self.username)


class Produit(models.Model):
    name = models.CharField('Nom', max_length=100)
    version = models.CharField('Version', max_length=10)
    description = models.CharField('Description', max_length=300)
    dateCreation = models.DateTimeField(default=timezone.now)

    class Meta:
     unique_together = ("name", "version",)

    def __str__(self):
        return "{}".format(self.name)


class Ticket(models.Model):
    titre = models.CharField('Objet du ticket', max_length=100)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    initiateur = models.ForeignKey(User, on_delete=models.CASCADE)
    dateOuverture = models.DateTimeField(default=timezone.now)
    description = models.CharField('Description', max_length=300)
    solution = models.CharField('Solution', max_length=5000)

    class Meta:
        unique_together = ("titre", "produit", "initiateur", "description", "solution")

    def __str__(self):
        return "{}".format(self.titre)


class Categorie(models.Model):
    name = models.CharField('Nom', max_length=100)
    tickets = PickledObjectField()
    supports = PickledObjectField()
    date = models.DateTimeField(default=timezone.now)
    description = models.CharField('Description', max_length=300)

    class Meta:
        ordering = ["-date",]
        unique_together = ("name",)

    def __str__(self):
        return "{}".format(self.name)


class Assignation(models.Model):
    SEVERITY = (
        ('Faible', 'Faible'),
        ('Moyen', 'Moyen'),
        ('Eleve', 'Eleve'),
    )

    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    support = models.ForeignKey(User, on_delete=models.CASCADE)
    gravite = models.CharField('Gravite-Ticket', choices=SEVERITY, max_length=50)
    etat = models.CharField('Etat-Ticket', max_length=50)
    delai = models.DateTimeField(default=timezone.now)
    dateAssignation = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["-dateAssignation",]
        unique_together = ("categorie", "ticket", "support")

    def __str__(self):
        return "{}".format(self.ticket.titre)
