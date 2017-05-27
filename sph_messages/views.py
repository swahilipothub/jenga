from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from sms import secrets
from contacts.models import Contact, Contact_Group

from .AfricasTalkingGateway import AfricasTalkingGateway, AfricasTalkingGatewayException
from .forms import SmsSettingsForm, SmsForm
from .models import Sms, SmsSettings


username = secrets.USERNAME
apikey   = secrets.APIKEY
gateway  = AfricasTalkingGateway(username, apikey)


@login_required(login_url='/login/')
def sms_settings_list(request):
    sms_settings_list = SmsSettings.objects.all()
    return render(request, 'settings_list.html', {'sms_settings_list': sms_settings_list})


@login_required(login_url='/login/')
def sms_settings_add(request):
    if request.method == 'POST':
        form = SmsSettingsForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['user_name']
            api_key   = form.cleaned_data['api_key']
            form.save()
            form      = SmsSettingsForm()
            messages.success(request, "Settings Successfully Added")
    else:
        form = SmsSettingsForm()
    return render(request, 'settings_add.html', {'form': form})


@login_required(login_url='/login/')
def sms_settings_update(request, pk):
    sms_settings_update = get_object_or_404(SmsSettings, pk=pk)
    if request.method == 'POST':
        form = SmsSettingsForm(request.POST, instance=sms_settings_update)
        if form.is_valid():
            user_name = form.cleaned_data['user_name']
            api_key   = form.cleaned_data['api_key']
            form.save()
            messages.success(request, "Settings Successfully Updated")
    else:
        form = SmsSettingsForm(instance=sms_settings_update)
    return render(request, 'settings_update.html', {'form': form})


@login_required(login_url='/login/')
def sms_list(request):
    sms_list = Sms.objects.all()
    return render(request, 'sms_list.html', {'sms_list': sms_list})


@login_required(login_url='/login/')
def sms_create(request):
    if request.method == 'POST':
        form = SmsForm(request.POST)
        if form.is_valid():
            category = form.cleaned_data['category']
            message  = form.cleaned_data['message']

            category_name = Contact_Group.objects.get(name=category)
            category_id   = category_name.id
            recipients    = Contact.objects.values_list('mobile', flat=True).filter(category=category_id)
            to            = ",".join(recipients)
            results       = gateway.sendMessage(to, message)

            form.save()
            form = SmsForm()
            messages.success(request, "Message Successfully Sent")
    else:
        form = SmsForm()
    return render(request, 'sms_create.html', {'form': form})