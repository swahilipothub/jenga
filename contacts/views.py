from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, get_object_or_404

from .models import Contact, Contact_Group
from .forms import ContactForm, Contact_GroupForm


contact_object = Contact.objects.all()


# Contact list.
@login_required(login_url='/login/')
def contact_list(request):
    contacts = contact_object
    return render(request, 'contacts.html', {'contacts': contacts})


@login_required(login_url='/login/')
def contact_create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            id_number = form.cleaned_data['id_number']
            mobile = form.cleaned_data['mobile']
            category = form.cleaned_data['category']
            form.save()
            form = ContactForm()
            messages.success(request, "Successfully Created")
    else:
        form = ContactForm()
    return render(request, 'contact_create.html', {'form': form})


"""Detail of a person.
   :param template: Add a custom template.
"""
@login_required(login_url='/login/')
def contact_detail(request, pk, template='contact_detail.html'):
    try:
        contact_detail = Contact.objects.get(pk__iexact=pk)
    except Contact.DoesNotExist:
        raise Http404

    kwvars = {
        'object': contact_detail,
    }

    return render_to_response(template, kwvars, RequestContext(request))


@login_required(login_url='/login/')
def contact_update(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            id_number = form.cleaned_data['id_number']
            mobile = form.cleaned_data['mobile']
            category = form.cleaned_data['category']
            form.save()
            messages.success(request, "Successfully Created")
    else:
        form = ContactForm(instance=contact)
    return render(request, 'contact_update.html', {'form': form})


@login_required(login_url='/login/')
def group_list(request):
    groups = contact_object
    return render(request, 'group_list.html', {'groups': groups})


@login_required(login_url='/login/')
def group_create(request):
    if request.method == 'POST':
        form = Contact_GroupForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            form.save()
            form = Contact_GroupForm()
    else:
        form = Contact_GroupForm()
    return render(request, 'group_create.html', {'form': form})


@login_required(login_url='/login/')
def group_update(request, pk):
    group = get_object_or_404(Contact_Group, pk=pk)
    if request.method == 'POST':
        form = Contact_GroupForm(request.POST, instance=group)
        if form.is_valid():
            name = form.cleaned_data['name']
            form.save()
    else:
        form = Contact_GroupForm(instance=group)
    return render(request, 'group_update.html', {'form': form})