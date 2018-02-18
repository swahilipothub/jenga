from django import forms
# from django.forms.formsets import BaseFormSet
# from django.forms.models import modelformset_factory

from .models import Contact, Contact_Group


class Contact_GroupForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))

    class Meta:
        model = Contact_Group
        fields = ('name', )


class ContactForm(forms.ModelForm):
    full_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    mobile = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    category = forms.ModelChoiceField(
        queryset=None, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Contact
        fields = ('full_name', 'mobile', 'category')

    def __init__(self, user, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['category'].queryset = Contact_Group.objects.filter(user=user)

# BaseContactFormSet = modelformset_factory(Contact, form=ContactForm, extra=4, can_delete=True)


class UploadFileForm(forms.Form):
    file = forms.FileField()
