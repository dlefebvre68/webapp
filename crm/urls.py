from django.conf.urls import url
from . import views

urlpatterns = [
   url(r'^$', views.IndexView.as_view(), name='index'),
   url(r'^contact_detail/(?P<contact_id>[0-9]+)/$', views.contact_detail, name='contact detail'),
   url(r'^update_contact/(?P<contact_id>[0-9]+)/$', views.update_contact, name='update contact'),
   url(r'^liste_contacts/$', views.liste_contacts, name='liste contacts'),
   url(r'^chercher_contacts/$', views.chercher_contacts, name='chercher contacts'),
   url(r'^faire_recherche/$', views.faire_recherche, name='faire recherche'),
   url(r'^nouveau_contact/$', views.nouveau_contact, name='nouveau contact'),
   url(r'^ajouter_contact/$', views.ajouter_contact, name='ajouter contact'),
   url(r'^generer_contact_csv/$', views.generer_contact_csv, name='generer contact csv'),
   url(r'^ajouter_note/(?P<contact_id>[0-9]+)/$', views.ajouter_note, name='ajouter note'),
   url(r'^ajouter_don/(?P<contact_id>[0-9]+)/$', views.ajouter_don, name='ajouter don'),
]

