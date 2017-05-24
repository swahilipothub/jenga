from django import forms
from django.shortcuts import render
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required

from django.contrib.admin.widgets import FilteredSelectMultiple

from AfricasTalkingGateway import AfricasTalkingGateway, AfricasTalkingGatewayException

from .models import Sms
from contacts.models import Contact

from sms import secrets

username = secrets.USERNAME
apikey   = secrets.APIKEY
gateway  = AfricasTalkingGateway(username, apikey)

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

            results = gateway.sendMessage(to, message)

            form.save()

            form = SmsForm()
    else:
        form = SmsForm()
    return render(request, 'sms_create.html', {'form': form})


# @login_required(login_url='/login/')
# def sms_fetch_list(request):
#     lastReceivedId = 0
#     while True:
#         messages = gateway.fetchMessages(lastReceivedId)
#         for sms_message in messages:
#             sms_from = message['from']
#             sms_to = message['to']
#             sms_date = message['date']
#             sms_text = message['text']
#             sms_linkID = message['linkID']  
#     return render(request, 'sms_list.html', {'sms_message': sms_message})