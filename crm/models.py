import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

class TypeDon(models.Model):
   type_don = models.CharField(max_length = 100, default="")

   def __str__(self):
      return self.type_don

class Categorie(models.Model):
   categorie = models.CharField(max_length = 100, default="")

   def __str__(self):
      return self.categorie

class StatutContact(models.Model):
   statut = models.CharField(max_length = 50)

   def __str__(self):
      return self.statut

class StatutCampagne(models.Model):
   statut = models.CharField(max_length = 50)

   def __str__(self):
      return self.statut

class Organisation(models.Model):
   nom = models.CharField(max_length = 100, default="")
   date_entree = models.DateTimeField('Date entree', blank=True, default="")
   telephone = models.CharField(max_length = 20, default="")
   adresse1 = models.CharField(max_length = 50, default="")
   adresse2 = models.CharField(max_length = 50, blank=True, default="")
   ville = models.CharField(max_length = 50, default="")
   province = models.CharField(max_length = 10, default="")
   code_postal = models.CharField(max_length = 7, default="")

   def __str__(self):
      return self.nom

class Contact(models.Model):
   salutation = models.CharField(max_length = 10, default="")
   nom = models.CharField(max_length = 100, default="")
   prenom = models.CharField(max_length = 100, default="")
   titre = models.CharField(max_length = 100, default="")
   telephone = models.CharField(max_length = 20, default="")
   autre_telephone = models.CharField(max_length = 20, default="")
   courriel = models.CharField(max_length = 50, default="")
   autre_courriel = models.CharField(max_length = 50, default="")
   categorie = models.ForeignKey(Categorie, default="")
   organisation = models.CharField(max_length = 100, blank=True, default="")
   date_entree = models.DateField("Date d'inscription", default="2008-01-01")
   adresse1 = models.CharField(max_length = 50, default="")
   adresse2 = models.CharField(max_length = 50, blank=True, default="")
   ville = models.CharField(max_length = 50, default="")
   province = models.CharField(max_length = 10, default="")
   code_postal = models.CharField(max_length = 7, default="")
   statut_contact = models.ForeignKey(StatutContact)
   statut_campagne = models.ForeignKey(StatutCampagne)
   carte_noel = models.BooleanField(default=False)

   def __str__(self):
      return self.nom + ',' + self.prenom
 
class Notes(models.Model):
   date = models.DateField()
   texte = models.CharField(max_length = 2000, default="")
   contact = models.ForeignKey(Contact)
   utilisateur = models.CharField(max_length = 50, default="")

   def __str__(self):
      return self.texte

class Dons(models.Model):
   annee = models.IntegerField()
   don = models.IntegerField(default = 0)
   type_don = models.ForeignKey(TypeDon, default="")
   contact = models.ForeignKey(Contact)
