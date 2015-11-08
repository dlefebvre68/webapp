from django.contrib import admin

from .models import Contact
from .models import Notes
from .models import StatutCampagne
from .models import StatutContact
from .models import Categorie
from .models import TypeDon
from .models import Dons

# Register your models here.

admin.site.register(Contact)
admin.site.register(StatutContact)
admin.site.register(StatutCampagne)
admin.site.register(Notes)
admin.site.register(Categorie)
admin.site.register(Dons)
admin.site.register(TypeDon)
