from django.contrib import admin
from core.models import *

models = [News, Contacts, Doctors, Advice, Address, Service, AboutUs, Feedback]
admin.site.register(models)