from django import forms

from .models import Contact, Contact_Group


class Contact_GroupForm(forms.ModelForm):
	name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

	class Meta:
		model = Contact_Group
		fields = ('name',)


class ContactForm(forms.ModelForm):
	first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	id_number = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	mobile = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	category = forms.ModelChoiceField(queryset=Contact_Group.objects.all(), 
										widget=forms.Select(attrs={'class':'form-control'}))

	# def __init__(group, *args, **args):
	# 	super(ContactForm,self ).__init__(group,*args,**kwargs)
	# 	self.fields['category'].queryset = Contact.objects.filter(user=request.user)

	class Meta:
		model  = Contact
		fields = ('first_name', 'last_name', 'id_number', 'mobile', 'category')

		
