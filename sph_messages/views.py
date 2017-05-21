from django import forms
from django.shortcuts import render
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required

from django.contrib.admin.widgets import FilteredSelectMultiple

from AfricasTalkingGateway import AfricasTalkingGateway, AfricasTalkingGatewayException

from .models import Sms
from contacts.models import Contact

username = "athmanziri"
apikey   = "6083c1f67ac28d2fb5525ed9be1ffac58a1fcda9998fc9d64ba672ef1baf9414"


class SmsForm(forms.ModelForm):
    to = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    # to = forms.ModelMultipleChoiceField(queryset=Contact.objects.all(), widget=FilteredSelectMultiple("verbose name", is_stacked=False))
    message = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
    class Meta:
        model = Sms
        fields = ('to', 'message')


@login_required(login_url='/login/')
def sms_list(request):
    sms_list = Sms.objects.all()
    return render(request, 'sms_list.html', {'sms_list': sms_list})


@login_required(login_url='/login/')
def sms_create(request):
    if request.method == 'POST':
        form = SmsForm(request.POST)

        if form.is_valid():
            to = form.cleaned_data['to']
            # cat = Contact.objects.all().filter(category=category)
            message = form.cleaned_data['message']

            gateway = AfricasTalkingGateway(username, apikey)

            results = gateway.sendMessage(to, message)

            form.save()

            form = SmsForm()
    else:
        form = SmsForm()
    return render(request, 'sms_create.html', {'form': form})