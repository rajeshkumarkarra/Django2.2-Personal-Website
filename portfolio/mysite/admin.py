from django.contrib import admin
from . models import Client, Contact

# Register your models here.
# models are database layers

admin.site.register(Client)
admin.site.register(Contact)
