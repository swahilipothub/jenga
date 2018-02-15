from django import forms
from django.forms.formsets import BaseFormSet

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


class BaseContactFormSet(BaseFormSet):
    def clean(self):
        """
        Adds validation to check that no two contacts have the same full name or mobile
        and that all contacts have both an full name, mobile and category.
        """
        if any(self.errors):
            return

        full_names = []
        mobiles = []
        categories = []
        duplicates = False

        for form in self.forms:
            if form.cleaned_data:
                full_name = form.cleaned_data['full_name']
                mobile = form.cleaned_data['mobile']
                category = form.cleaned_data['category']

                # Check that no two contacts have the same full_name or URL
                if full_name and mobile and category:
                    if full_name in full_names:
                        duplicates = True
                    full_names.append(full_name)

                    if mobile in mobiles:
                        duplicates = True
                    mobiles.append(mobile)

                if duplicates:
                    raise forms.ValidationError(
                        'Contacts must have unique full_names and mobile numbers.',
                        code='duplicate_links'
                    )

                # Check that all contacts have both an full_name and mobile number
                if mobile and not (full_name and category):
                    raise forms.ValidationError(
                        'All contacts must have an full_name.',
                        code='missing_full_name'
                    )
                elif full_name and not (mobile and category):
                    raise forms.ValidationError(
                        'All contacts must have a mobile number.',
                        code='missing_mobile'
                    )
                elif category and not (mobile and full_name):
                    raise forms.ValidationError(
                        'All contacts must have a group category.',
                        code='missing_category')


class UploadFileForm(forms.Form):
    file = forms.FileField()
