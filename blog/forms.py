from django import forms
from django.forms import ModelForm
from django.forms import TextInput
from .models import Produit

class ProduitForm(ModelForm):
    	class Meta :
         model = Produit
         fields = ['type_de_produit', 'poids', 'numero', 'imageProduit1','imageProduit2','imageProduit3']
         widgets = {
				'type_de_produit': TextInput(attrs={'placeholder':'Nom du Produit','class':'form-control'}),
				'numero': TextInput(attrs={'placeholder':'225 XX XX XX XX XX (Votre numéro de téléphone)','class':'form-control'}),
			}