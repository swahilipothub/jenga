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
	category = forms.ModelChoiceField(queryset=None, 
									widget=forms.Select(attrs={'class':'form-control'}))

	class Meta:
		model  = Contact
		fields = ('first_name', 'last_name', 'id_number', 'mobile', 'category')

		
	def __init__(self, user, *args, **kwargs):
	    super(ContactForm, self).__init__(*args, **kwargs)
	    self.fields['category'].queryset = Contact_Group.objects.filter(user=user)


class UploadFileForm(forms.Form):
    file = forms.FileField()