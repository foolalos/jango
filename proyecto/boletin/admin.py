# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .forms import RegModelForm, ContactForm
from .models import Registrado

class AdminRegistrado(admin.ModelAdmin):
	list_display = ["email", "nombre", "timestamp", "carrera"]
	form = RegModelForm
	#list_display_links = ["nombre"]
	list_filter = ["timestamp"]
	list_editable = ["nombre"]
	list_editable = ["carrera"]
	search_fields = ["email", "nombre", "carrera"]
	#class Meta:
	#	model= Registrado

admin.site.register(Registrado, AdminRegistrado)
