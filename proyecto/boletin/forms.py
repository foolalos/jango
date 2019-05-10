from django import forms

from .models import Registrado

class RegModelForm(forms.ModelForm):
	class Meta:
		model = Registrado
		fields = ["nombre","email","carrera"]

	def clean_email(self):
		email = self.cleaned_data.get("email")
		email_base, proveeder = email.split("@")
		dominio, extension = proveeder.split(".")
		if not extension == "com":
			raise forms.ValidationError("Utiliza la extension .EDU")
		return email

	def clean_nombre(self):
		nombre = self.cleaned_data.get("nombre")
		#validaciones
		return nombre

	def clean_semestre(self):
		semestre = self.cleaned_data.get("carrera")
				#validaciones
		return semestre

class ContactForm(forms.Form):
	nombre = forms.CharField(required=False)
	email = forms.EmailField()
	mensaje = forms.CharField(widget=forms.Textarea)
	carrera = forms.CharField(required=False)


   # def clean_email(self):
	#	email = self.cleaned_data.get("email")
	#	email_base, proveeder = email.split("@")
	#	dominio, extension = proveeder.split(".")
	#	if not extension == "edu":
	#		raise forms.ValidationError("Utiliza la extension .EDU")
	#	return email
