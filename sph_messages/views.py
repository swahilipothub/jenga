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
sender = "Jenga"


@login_required
def sms_settings_list(request):
    sms_settings_list = SmsSettings.objects.filter(user=request.user)
    return render(request, 'sph_messages/settings_list.html', {'sms_settings_list': sms_settings_list})


@login_required(login_url='/login/')
def sms_settings_add(request):
    if request.method == 'POST':
        form = SmsSettingsForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['user_name']
            api_key = form.cleaned_data['api_key']

            settings_add = form.save(commit=False)
            settings_add.user = request.user
            settings_add.save()

            form = SmsSettingsForm()
            messages.success(request, "Settings Successfully Added")
    else:
        form = SmsSettingsForm()
    return render(request, 'sph_messages/settings_add.html', {'form': form})


@login_required
def sms_settings_update(request, pk):
    sms_settings_update = get_object_or_404(SmsSettings, pk=pk)
    if request.method == 'POST':
        form = SmsSettingsForm(request.POST, instance=sms_settings_update)
        if form.is_valid():
            user_name = form.cleaned_data['user_name']
            api_key = form.cleaned_data['api_key']

            settings_update = form.save(commit=False)
            settings_update.user = request.user
            settings_update = form.save()

            messages.success(request, "Settings Successfully Updated")
    else:
        form = SmsSettingsForm(instance=sms_settings_update)
    return render(request, 'sph_messages/settings_update.html', {'form': form})


@login_required
def sms_list(request):
    sms_list = Sms.objects.filter(user=request.user)
    return render(request, 'sph_messages/sms_list.html', {'sms_list': sms_list})


@login_required
def sms_create(request):
    if request.method == 'POST':
        form = SmsForm(request.user, request.POST)
        bulkSMSMode = 1
        sender = None
        enqueue = 1

        if form.is_valid():
            category = form.cleaned_data['category']
            message  = form.cleaned_data['message']

            category_name = Contact_Group.objects.get(name=category)
            category_id   = category_name.id
            recipients    = Contact.objects.values_list('mobile', flat=True).filter(category=category_id)
            to            = ",".join(recipients)
            results       = gateway.sendMessage(to, message, sender, bulkSMSMode, enqueue)

            sms_create = form.save(commit=False)
            sms_create.user = request.user
            sms_create.save()
            form = SmsForm(request.user)
            messages.success(request, "Message Successfully Sent")
    else:
        form = SmsForm(request.user)
    return render(request, 'sph_messages/sms_create.html', {'form': form})


@login_required
def sms_fetch(request, template_name='sph_messages/fetch_messages.html'):
    lastReceivedId = 0;    
    while True:
        messages = gateway.fetchMessages(lastReceivedId)
        for message in messages:
            message_from = message['from']
            messate_to = message['to']
            message_date = message['date']
            message_text = message['text']
            message_linkID = message['linkID']
            lastReceivedId = message['id']

            return render(request, template_name, {'object':message})


@login_required
def user_balance(request):
    try:
        user = gateway.getUserData()
        balance = user['balance']
        return render(request, 'sph_messages/balance.html', {'object': balance})
    except AfricasTalkingGatewayException as e:
        print ('Error: %s') % str(e)