from django.contrib.auth.decorators import login_required

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string

from .models import Contact, Sms, Contact_Group
from .forms import ContactForm, SmsForm, Contact_GroupForm

from django.contrib import messages


# @login_required(login_url='/login/')
def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'contact_list.html', {'contacts': contacts})


# @login_required(login_url='/login/')
def contact_create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            id_number = form.cleaned_data['id_number']
            mobile = form.cleaned_data['mobile']

            form.save()

            messages.success(request, "Successfully Created")
    else:
        form = ContactForm()
    return render(request, 'contact_create.html', {'form': form})


def group_list(request):
    groups = Contact_Group.objects.all()
    return render(request, 'group_list.html', {'groups': groups})


def group_create(request):
    if request.method == 'POST':
        form = Contact_GroupForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            contacts = form.cleaned_data['contacts']

            form.save()
    else:
        form = Contact_GroupForm()
    return render(request, 'group_create.html', {'form': form})


def group_update(request):
    group = get_object_or_404(Contact_Group, pk=pk)
    if request.method == 'POST':
        form = Group_ContactForm(request.POST, instance=group)
    else:
        form = Group_ContactForm(instance=group)
    return render(request, 'group_update.html', {'form': form})
