from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from contacts.models import Contact, Contact_Group
from .AfricasTalkingGateway import AfricasTalkingGateway, AfricasTalkingGatewayException
from .forms import SmsForm
from .models import Sms

username = settings.AFRICASTALKING_USERNAME
apikey   = settings.AFRICASTALKING_APIKEY
gateway  = AfricasTalkingGateway(username, apikey)
sender = "Jenga"


@login_required
def sms_list(request):
    sms_list = Sms.objects.filter(user=request.user)
    return render(request, 'msgs/sms_list.html', {'sms_list': sms_list})


@login_required
def sms_create(request):
    if request.method == 'POST':
        form = SmsForm(request.user, request.POST)
        bulkSMSMode = 1
        sender = None
        enqueue = 1

        if form.is_valid():
            category = form.cleaned_data['category']
            message = form.cleaned_data['message']

            category_name = Contact_Group.objects.get(name=category)
            category_id = category_name.id
            recipients = Contact.objects.values_list('mobile', 
                                                    flat=True).filter(
                                                    category=category_id)
            to  = ",".join(recipients)

            try:
                results = gateway.sendMessage(to, message, sender, bulkSMSMode, enqueue)
                for recipient in results:
                    sms = form.save(commit=False)
                    sms.user = request.user
                    sms.number = recipient['number']
                    sms.messageId = recipient['messageId']
                    sms.status = recipient['status']
                    sms.cost = recipient['cost']
                    sms.save()
                messages.success(request, "Message Successfully Sent")
            except AfricasTalkingGatewayException as e:
                messages.warning('Encountered an error while sending: %s' % str(e))
    else:
        form = SmsForm(request.user)
    return render(request, 'msgs/sms_create.html', {'form': form})


@login_required
def sms_fetch(request, template_name='msgs/fetch_messages.html'):
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
        return render(request, 'msgs/balance.html', {'object': balance})
    except AfricasTalkingGatewayException as e:
        print ('Error: %s') % str(e)