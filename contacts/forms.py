from django import forms

from .models import Contact, Contact_Group


# CONTACTS = [(x.mobile, x.first_name) for x in Contact.objects.all()]

class Contact_GroupForm(forms.ModelForm):
	name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	# contact = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple())
	# contact = forms.MultipleChoiceField(choices=CONTACTS, widget=forms.CheckboxSelectMultiple(), required=False)

	class Meta:
		model = Contact_Group
		fields = ('name',)


class ContactForm(forms.ModelForm):
	first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	id_number = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	mobile = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	category = forms.ModelChoiceField(queryset=Contact_Group.objects.all())

	class Meta:
		model  = Contact
		fields = ('first_name', 'last_name', 'id_number', 'mobile', 'category')
