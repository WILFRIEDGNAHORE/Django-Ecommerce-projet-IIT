from django import forms
from .models import ShippingAddress

class ShippingForm(forms.ModelForm):
	shipping_full_name = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nom complet'}), required=True)
	shipping_email = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}), required=True)
	shipping_address1 = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address1'}), required=True)
	shipping_address2 = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address2'}), required=False)
	shipping_city = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ville'}), required=True)
	shipping_state = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'État'}), required=False)
	shipping_zipcode = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Code postal'}), required=False)
	shipping_country = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Pays'}), required=True)

	class Meta:
		model = ShippingAddress
		fields = ['shipping_full_name', 'shipping_email', 'shipping_address1', 'shipping_address2', 'shipping_city', 'shipping_state', 'shipping_zipcode', 'shipping_country']

		exclude = ['user',]


class PaymentForm(forms.Form):
	card_name =  forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nom sur la carte'}), required=True)
	card_number =  forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Numero de la carte'}), required=True)
	card_exp_date =  forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':"Date d'expiration"}), required=True)
	card_cvv_number =  forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'CVV Code'}), required=True)
	card_address1 =  forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Addresse de livraison 1'}), required=True)
	card_address2 =  forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Addresse de livraison 2'}), required=False)
	card_city =  forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ville de facturation'}), required=True)
	card_state = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'État de facturation'}), required=True)
	card_zipcode =  forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Code postal de facturation'}), required=True)
	card_country =  forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Pays de facturation'}), required=True)