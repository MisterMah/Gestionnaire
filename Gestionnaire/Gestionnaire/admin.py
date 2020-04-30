from django.contrib import admin
from import_export import resources # For export data
from .models import (
    Produit,
    Ticket,
    Categorie,
    Assignation,
)

class ProduitResource(resources.ModelResource):
    class Meta:
        model = Produit

class TicketResource(resources.ModelResource):
    class Meta:
        model = Ticket

class CategorieResource(resources.ModelResource):
    class Meta:
        model = Categorie

class AssignationResource(resources.ModelResource):
    class Meta:
        model = Assignation


class ProduitAdmin(admin.ModelAdmin):
    list_display = ["name", "version", "description", "dateCreation",]
    search_fields = ["name", "description", "version"]


class TicketAdmin(admin.ModelAdmin):
    list_display = ["titre", "produit", "initiateur", "dateOuverture", "description", "solution" ]
    search_fields = ["titre", "produit__name", "initiateur"]


class CategorieAdmin(admin.ModelAdmin):
    list_display = ["name", "tickets", "supports", "date", "description"]
    search_fields = ["name", "ticket__titre", "support__username", "support__first_name", "support__last_name", "description"]

class AssignationAdmin(admin.ModelAdmin):
    list_display = ["categorie", "ticket", "support", "gravite", "etat", "delai", "dateAssignation"]
    search_fields = ["categorie__name", "ticket__titre", "support__username", "gravite", "etat",]


admin.site.register (Produit, ProduitAdmin)
admin.site.register (Ticket, TicketAdmin)
admin.site.register (Categorie, CategorieAdmin)
admin.site.register (Assignation, AssignationAdmin)
