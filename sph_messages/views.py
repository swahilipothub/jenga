from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from sms import secrets
from contacts.models import Contact, Contact_Group

from .AfricasTalkingGateway import AfricasTalkingGateway, AfricasTalkingGatewayException
from .forms import SmsForm
from .models import Sms


username = secrets.USERNAME
apikey   = secrets.APIKEY
gateway  = AfricasTalkingGateway(username, apikey)
sender = "Jenga"


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
            group_contacts = Contact.objects.values_list('first_name', flat=True).filter(category=category_id)
            sms_create.recipient_list = ",".join(group_contacts)
            sms_create.recipient_count = group_contacts.count()

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