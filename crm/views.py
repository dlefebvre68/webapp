import csv
from datetime import datetime
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from django.views import generic
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .models import Contact, StatutContact, StatutCampagne, Dons, TypeDon
from .models import Organisation, Notes, Categorie

class IndexView(generic.ListView):
   template_name = 'crm/index.html'
   
   context_object_name = 'contact_list'

   def get_queryset(self):
      return Contact.objects.order_by('nom', 'prenom')

class ContactView(generic.DetailView):
   model = Contact
   template_name = 'crm/contact_detail.html'

# Create your views here.

def index(request):
   contact_list = Contact.objects.order_by('nom', 'prenom')
   context = {'contact_list': contact_list,}
   return render(request, 'crm/index.html', context)

def liste_contacts(request):
   contact_list = Contact.objects.order_by('nom', 'prenom')
   prenom = ""
   nom = ""
   organisation = ""
   statut_contact = ""
   statut_campagne = ""
   categorie = ""
   context = {'contact_list': contact_list,
              'prenom': prenom,
              'nom': nom,
              'organisation': organisation,
              'statut_contact': statut_contact,
              'statut_campagne': statut_campagne,
              'categorie': categorie,}
   return render(request, 'crm/liste_contacts.html', context)

def liste_org(request):
   org_list = Organisation.objects.order_by('nom')
   context = {'org_list': org_list,}
   return render(request, 'crm/liste_org.html', context)

def chercher_contacts(request):
   statut_contact_list = [""]
   for statut in StatutContact.objects.all():
      statut_contact_list.append(statut.statut)
   statut_campagne_list = [""]
   for statut in StatutCampagne.objects.all():
      statut_campagne_list.append(statut.statut)
   categorie_list = [""]
   for categorie in Categorie.objects.all():
      categorie_list.append(categorie.categorie)
   context = {'statut_contact_list': statut_contact_list,
              'statut_campagne_list': statut_campagne_list,
              'categorie_list': categorie_list,}
   return render(request, 'crm/chercher_contacts.html', context)

def retourner_resultat_recherche(prenom, nom, organisation, statut_contact, statut_campagne, categorie):
   contact_list = Contact.objects.all()
   if prenom != '':
      contact_list = contact_list.filter(prenom__contains = prenom)
   if nom != '':
      contact_list = contact_list.filter(nom__contains = nom)
   if organisation != '':
      contact_list = contact_list.filter(organisation__contains = organisation)
   if statut_contact != '':
      contact_list = contact_list.filter(statut_contact__statut = statut_contact)
   if statut_campagne != '':
      contact_list = contact_list.filter(statut_campagne__statut = statut_campagne)
   if categorie != '':
      contact_list = contact_list.filter(categorie__categorie = categorie)

   return contact_list

def faire_recherche(request):
   prenom = request.POST['prenom']
   nom = request.POST['nom']
   organisation = request.POST['organisation']
   statut_contact = request.POST['statut_contact']
   statut_campagne = request.POST['statut_campagne']
   categorie = request.POST['categorie']

   contact_list = retourner_resultat_recherche(prenom, nom, organisation, statut_contact, statut_campagne, categorie)
   context = {'contact_list': contact_list,
              'prenom': prenom,
              'nom': nom,
              'organisation': organisation,
              'statut_contact': statut_contact,
              'statut_campagne': statut_campagne,
              'categorie': categorie,}
   return render(request, 'crm/liste_contacts.html', context)

def contact_detail(request, contact_id):
   contact = get_object_or_404(Contact, pk=contact_id)
   prenom = request.POST['prenom']
   nom = request.POST['nom']
   organisation = request.POST['organisation']
   statut_contact = request.POST['statut_contact']
   statut_campagne = request.POST['statut_campagne']
   categorie = request.POST['categorie']
   statut_contact_list = StatutContact.objects.all()
   statut_campagne_list = StatutCampagne.objects.all()
   categorie_list = Categorie.objects.all()
   type_don_list = TypeDon.objects.all()
   context = {'contact': contact,
              'prenom': prenom,
              'nom': nom,
              'organisation': organisation,
              'statut_contact': statut_contact,
              'statut_campagne': statut_campagne,
              'categorie': categorie,
              'statut_contact_list': statut_contact_list,
              'statut_campagne_list': statut_campagne_list,
              'categorie_list': categorie_list,
              'type_don_list': type_don_list,}
   return render(request, 'crm/contact_detail.html', context)

def nouveau_contact(request):
   statut_contact_list = StatutContact.objects.all()
   statut_campagne_list = StatutCampagne.objects.all()
   categorie_list = Categorie.objects.all()
   context = { 'statut_contact_list': statut_contact_list,
               'statut_campagne_list': statut_campagne_list,
               'categorie_list': categorie_list,}
   return render(request, 'crm/nouveau_contact.html', context)

def ajouter_contact(request):
   contact = Contact()
   contact.salutation = request.POST['salutation']
   contact.prenom = request.POST['prenom']
   contact.nom = request.POST['nom']
   contact.titre = request.POST['titre']
   contact.telephone = request.POST['telephone']
   contact.autre_telephone = request.POST['autre_telephone']
   contact.courriel = request.POST['courriel']
   contact.autre_courriel = request.POST['autre_courriel']
   contact.organisation = request.POST['organisation']
   contact.date_entree = request.POST['date_entree']
   contact.adresse1 = request.POST['adresse1']
   contact.adresse2 = request.POST['adresse2']
   contact.ville = request.POST['ville']
   contact.province = request.POST['province']
   contact.code_postal = request.POST['code_postal']
   contact.categorie = Categorie.objects.get(pk=int(request.POST['categorie']))
   contact.statut_contact = StatutContact.objects.get(pk=int(request.POST['statut_contact']))
   contact.statut_campagne = StatutCampagne.objects.get(pk=int(request.POST['statut_campagne']))
   contact.save()
   return HttpResponseRedirect(reverse('crm:index'))

def ajouter_org(request):
   org = Organisation()
   org.nom = request.POST['nom']
   org.date_entree = request.POST['date_entree']
   org.telephone = request.POST['telephone']
   org.adresse1 = request.POST['adresse1']
   org.adresse2 = request.POST['adresse2']
   org.ville = request.POST['ville']
   org.province = request.POST['province']
   org.code_postal = request.POST['code_postal']
   org.save()
   return HttpResponseRedirect(reverse('crm:index'))

def update_contact(request, contact_id):
   contact = get_object_or_404(Contact, pk=contact_id)
   nouveau_salutation = request.POST['salutation']
   nouveau_prenom = request.POST['prenom']
   nouveau_nom = request.POST['nom']
   nouveau_titre = request.POST['titre']
   nouveau_telephone = request.POST['telephone']
   nouveau_autre_telephone = request.POST['autre_telephone']
   nouveau_courriel = request.POST['courriel']
   nouveau_autre_courriel = request.POST['autre_courriel']
   nouveau_organisation = request.POST['organisation']
   nouveau_date_entree = request.POST['date_entree']
   nouveau_adresse1 = request.POST['adresse1']
   nouveau_adresse2 = request.POST['adresse2']
   nouveau_ville = request.POST['ville']
   nouveau_province = request.POST['province']
   nouveau_code_postal = request.POST['code_postal']
   nouveau_categorie = int(request.POST['categorie'])
   nouveau_statut_contact = int(request.POST['statut_contact'])
   nouveau_statut_campagne = int(request.POST['statut_campagne'])
   if contact.salutation != nouveau_salutation:
      contact.salutation = nouveau_salutation
   if contact.prenom != nouveau_prenom:
      contact.prenom = nouveau_prenom
   if contact.nom != nouveau_nom:
      contact.nom = nouveau_nom
   if contact.titre != nouveau_titre:
      contact.titre = nouveau_titre
   if contact.telephone != nouveau_telephone:
      contact.telephone = nouveau_telephone
   if contact.autre_telephone != nouveau_autre_telephone:
      contact.autre_telephone = nouveau_autre_telephone
   if contact.courriel != nouveau_courriel:
      contact.courriel = nouveau_courriel
   if contact.autre_courriel != nouveau_autre_courriel:
      contact.autre_courriel = nouveau_autre_courriel
   if contact.organisation != nouveau_organisation:
      contact.organisation = nouveau_organisation
   if contact.date_entree != nouveau_date_entree:
      contact.date_entree = nouveau_date_entree
   if contact.adresse1 != nouveau_adresse1:
      contact.adresse1 = nouveau_adresse1
   if contact.adresse2 != nouveau_adresse2:
      contact.adresse2 = nouveau_adresse2
   if contact.ville != nouveau_ville:
      contact.ville = nouveau_ville
   if contact.province != nouveau_province:
      contact.province = nouveau_province
   if contact.code_postal != nouveau_code_postal:
      contact.code_postal = nouveau_code_postal
   if contact.categorie.id != nouveau_categorie:
      contact.categorie = Categorie.objects.get(pk=nouveau_categorie)
   if contact.statut_contact.id != nouveau_statut_contact:
      contact.statut_contact = StatutContact.objects.get(pk=nouveau_statut_contact)
   if contact.statut_campagne.id != nouveau_statut_campagne:
      contact.statut_campagne = StatutCampagne.objects.get(pk=nouveau_statut_campagne)
   contact.save()
   context = {'contact': contact,
              'statut_contact_list': StatutContact.objects.all(),}
   return render(request, 'crm/contact_detail.html', context)

def update_org(request, org_id):
   org = get_object_or_404(Organisation, pk=org_id)
   nouveau_nom = request.POST['nom']
   nouveau_date_entree = request.POST['date_entree']
   nouveau_telephone = request.POST['telephone']
   nouveau_adresse1 = request.POST['adresse1']
   nouveau_adresse2 = request.POST['adresse2']
   nouveau_ville = request.POST['ville']
   nouveau_province = request.POST['province']
   nouveau_code_postal = request.POST['code_postal']
   if org.nom != nouveau_nom:
      org.nom = nouveau_nom
   if org.date_entree != nouveau_date_entree:
      org.date_entree = nouveau_date_entree
   if org.telephone != nouveau_telephone:
      org.telephone = nouveau_telephone
   if org.adresse1 != nouveau_adresse1:
      org.adresse1 = nouveau_adresse1
   if org.adresse2 != nouveau_adresse2:
      org.adresse2 = nouveau_adresse2
   if org.ville != nouveau_ville:
      org.ville = nouveau_ville
   if org.province != nouveau_province:
      org.province = nouveau_province
   if org.code_postal != nouveau_code_postal:
      org.code_postal = nouveau_code_postal
   org.save()
   return HttpResponseRedirect(reverse('crm:index'))

def ajouter_note(request, contact_id):
   contact = get_object_or_404(Contact, pk=contact_id)
   contact.notes_set.create(texte=request.POST['note'], 
                            date=timezone.now(),
                            utilisateur="")
   statut_contact_list = StatutContact.objects.all()
   context = {'contact': contact,
              'statut_contact_list': statut_contact_list,}
   return render(request, 'crm/contact_detail.html', context)

def ajouter_don(request, contact_id):
   contact = get_object_or_404(Contact, pk=contact_id)
   contact.dons_set.create(don=request.POST['don'], 
                           annee=request.POST['annee'], 
                           type_don=TypeDon.objects.get(pk=request.POST['type_don']),)
   statut_contact_list = StatutContact.objects.all()
   context = {'contact': contact,
              'statut_contact_list': statut_contact_list,}
   return render(request, 'crm/contact_detail.html', context)

def generer_contact_csv(request):
   prenom = request.POST['prenom']
   nom = request.POST['nom']
   organisation = request.POST['organisation']
   statut_contact = request.POST['statut_contact']
   statut_campagne = request.POST['statut_campagne']
   categorie = request.POST['categorie']
   annee = request.POST['annee']

   contact_list = retourner_resultat_recherche(prenom, nom, organisation, statut_contact, statut_campagne, categorie, annee)
   response = HttpResponse(content_type='text/csv')
   response['Content-Disposition'] = 'attachment; filename="contact-' + datetime.now().strftime("%Y%m%d%H%M%S") + '.csv"'

   writer = csv.writer(response)
   writer.writerow(['Salutation',
                    'Prénom',
                    'Nom',
                    'Titre',
                    'Téléphone',
                    'Autre téléphone',
                    'Courriel',
                    'Autre courriel',
                    'Catégorie',
                    'Organisation',
                    'Adresse1',
                    'Adresse2',
                    'Ville',
                    'Province',
                    'Code Postal',
                    'Statut Contact',
                    'Statut Campagne',
                    'Don pour ' + annee])

   for contact in contact_list:
      writer.writerow([contact.salutation,
                       contact.prenom,
                       contact.nom,
                       contact.titre,
                       contact.telephone,
                       contact.autre_telephone,
                       contact.courriel,
                       contact.autre_courriel,
                       contact.categorie.categorie,
                       contact.organisation,
                       contact.adresse1,
                       contact.adresse2,
                       contact.ville,
                       contact.province,
                       contact.code_postal,
                       contact.statut_contact.statut,
                       contact.statut_campagne.statut,
                       ])
   return response
