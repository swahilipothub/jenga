from django import forms

from contacts.models import Contact_Group
from .models import Sms, SmsSettings


class SmsSettingsForm(forms.ModelForm):
    user_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    api_key = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = SmsSettings
        fields = ('user_name', 'api_key')


class SmsForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=None, 
                                      widget=forms.Select(attrs={'class':'form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
    class Meta:
        model = Sms
        fields = ('category', 'message')

    def __init__(self, user, *args, **kwargs):
        super(SmsForm, self).__init__(*args, **kwargs)
        self.fields['category'].queryset = Contact_Group.objects.filter(user=user)