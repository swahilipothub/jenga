from django import forms

from .models import Contact, Contact_Group, Sms


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'id_number', 'mobile')


class Contact_GroupForm(forms.ModelForm):
    class Meta:
        model = Contact_Group
        fields = ('name', 'contacts')


class SmsForm(forms.ModelForm):
    class Meta:
        model = Sms
        fields = ('group', 'sms')
