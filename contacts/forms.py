from django import forms

from .models import Contact, Contact_Group, Sms


class ContactForm(forms.ModelForm):
	first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	id_number = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	mobile = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

	class Meta:
		model  = Contact
		fields = ('first_name', 'last_name', 'id_number', 'mobile')


class Contact_GroupForm(forms.ModelForm):
	name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	# contacts = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple())

	class Meta:
		model = Contact_Group
		fields = ('name', 'contacts')


class SmsForm(forms.ModelForm):

	class Meta:
		model = Sms
		fields = ('group', 'sms')