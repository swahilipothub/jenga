import random
import logging

from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from contacts.models import Contact, Contact_Group
from .AfricasTalkingGateway import AfricasTalkingGateway, AfricasTalkingGatewayException
from .forms import SmsForm
from .models import Sms


@login_required
def sms_list(request):
    sms_list = Sms.objects.filter(user=request.user).order_by('-created')
    return render(request, 'msgs/sms_list.html', {'sms_list': sms_list})


@login_required
def sms_create(request):
    if request.method == 'POST':
        form = SmsForm(request.user, request.POST)
        username = request.user.profile.africastalking_username
        apikey = request.user.profile.africastalking_api_key
        sender = request.user.profile.africastalking_sender_id
        gateway = AfricasTalkingGateway(username, apikey)
        bulkSMSMode = 1
        enqueue = 1

        if form.is_valid():
            category = form.cleaned_data['category']
            message = form.cleaned_data['message']

            category_name = Contact_Group.objects.filter(id__in=category)
            for item in category_name:
                category_id = item.id
                recipients = Contact.objects.values_list(
                    'mobile', flat=True).filter(category=category_id).distinct().order_by()
                to = ",".join(recipients)

                try:
                    results = gateway.sendMessage(to, message, sender, bulkSMSMode, enqueue)
                    print(username)
                    for recipient in results:
                        user = request.user
                        message = message
                        number = recipient['number']
                        messageId = recipient['messageId']
                        status = recipient['status']
                        cost = recipient['cost']
                        instance = Sms.objects.create(user=user,
                                        message=message, number=number,
                                        messageId=messageId, status=status, cost=cost)
                        instance.category.set(category_name)
                except AfricasTalkingGatewayException as e:
                    messages.warning(request, 'Encountered an error while sending message')
                    logging.ERROR('Encountered an error while sending: {}'.format(e))
            messages.success(request, "Message Successfully delivered.")
    else:
        form = SmsForm(request.user)
    return render(request, 'msgs/sms_create.html', {'form': form})


@login_required
def sms_fetch(request, template_name='msgs/fetch_messages.html'):
    last_received_id = 0
    username = request.user.profile.africastalking_username
    apikey = request.user.profile.africastalking_api_key
    gateway = AfricasTalkingGateway(username, apikey)
    while True:
        messages = gateway.fetchMessages(last_received_id)
        for message in messages:
            message_from = message['from']
            messate_to = message['to']
            message_date = message['date']
            message_text = message['text']
            message_link_id = message['linkID']
            last_received_id = message['id']

            return render(request, template_name, {'object': message})


@login_required
def user_balance(request):
    username = request.user.profile.africastalking_username
    apikey = request.user.profile.africastalking_api_key
    gateway = AfricasTalkingGateway(username, apikey)
    try:
        user = gateway.getUserData()
        balance = user['balance']
        return render(request, 'msgs/balance.html', {'object': balance})
    except AfricasTalkingGatewayException as e:
        print('Error: %s') % str(e)
