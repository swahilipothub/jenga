from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Profile


class SignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    email = forms.EmailField(
        max_length=254,
        help_text='Required. Inform a valid email address.',
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )


class ProfileForm(forms.ModelForm):
    institution = forms.CharField(
        widget=forms.TextInput(attrs={ 'class': 'form-control' }), 
        max_length=50, 
        required=False)
    location = forms.CharField(widget=forms.TextInput(
        attrs={ 'class': 'form-control' }), 
        max_length=30, 
        required=False)
    public_email = forms.CharField(
        widget=forms.EmailInput(attrs={ 'class': 'form-control' }), 
        max_length=254, 
        required=False)
    africastalking_api_key = forms.CharField(
        widget=forms.TextInput(attrs={ 'class': 'form-control' }), 
        max_length=256, 
        required=False)
    africastalking_username = forms.CharField(
        widget=forms.TextInput(attrs={ 'class': 'form-control' }), 
        max_length=128, 
        required=False)
    africastalking_sender_id = forms.CharField(
        widget=forms.TextInput(attrs={ 'class': 'form-control' }), 
        max_length=128, 
        required=False)
    
    class Meta:
        model = Profile
        fields = ['institution', 'location', 'public_email',
            'africastalking_api_key', 'africastalking_username', 'africastalking_sender_id']

    def save(self, *args, **kwargs):
        u = self.instance.user
        u.save()
        profile = super(ProfileForm, self).save(*args, **kwargs)
        return profile
