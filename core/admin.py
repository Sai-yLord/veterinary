from django.contrib import admin
from core.models import *

class ContactInline(admin.TabularInline):
    model = Contact

class ContactsAdmin(admin.ModelAdmin):
    inlines = [ContactInline]

models = [News, Contact, Doctors, Advices, Address, Services, AboutUs, Feedback, Products]
admin.site.register(models)
admin.site.register(Contacts, ContactsAdmin)