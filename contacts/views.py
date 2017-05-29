from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect

from .models import Contact, Contact_Group
from .forms import ContactForm, Contact_GroupForm


# Contact list.
@login_required(login_url='/login/')
def contact_list(request):
    contacts = Contact.objects.filter(user=request.user).order_by('-created')
    return render(request, 'contacts/contacts.html', {'contacts': contacts})


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

            contact_create = form.save(commit=False)
            contact_create.user = request.user
            contact_create.save()

            form = ContactForm()
            messages.success(request, "Contact Successfully Created")
    else:
        form = ContactForm()
    return render(request, 'contacts/contact_create.html', {'form': form})


"""Detail of a person.
   :param template: Add a custom template.
"""
@login_required(login_url='/login/')
def contact_detail(request, pk, template='contacts/contact_detail.html'):
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

            contact_update = form.save(commit=False)
            contact_update.user = request.user
            contact_update.save()

            messages.success(request, "Contact Successfully Updated")
    else:
        form = ContactForm(instance=contact)
    return render(request, 'contacts/contact_update.html', {'form': form})


@login_required(login_url='/login/')
def contact_delete(request, pk, template_name='contacts/confirm_contact_delete.html'):
    contact = get_object_or_404(Contact, pk=pk)    
    if request.method=='POST':
        contact.delete()
        messages.success(request, "Contact Successfully Deleted")
        return redirect('contact_list')
    return render(request, template_name, {'object':contact})



@login_required(login_url='/login/')
def group_list(request):
    groups = Contact_Group.objects.filter(user=request.user).order_by('-created')
    return render(request, 'contacts/group_list.html', {'groups': groups})


@login_required(login_url='/login/')
def group_create(request):
    if request.method == 'POST':
        form = Contact_GroupForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']

            group = form.save(commit=False)
            group.user = request.user
            group.save()

            form = Contact_GroupForm()
            messages.success(request, "Group Successfully Created")
    else:
        form = Contact_GroupForm()
    return render(request, 'contacts/group_create.html', {'form': form})


@login_required(login_url='/login/')
def group_update(request, pk):
    group = get_object_or_404(Contact_Group, pk=pk)
    if request.method == 'POST':
        form = Contact_GroupForm(request.POST, instance=group)
        if form.is_valid():
            name = form.cleaned_data['name']

            group_update = form.save(commit=False)
            group_update.user = request.user
            group_update.save()

            messages.success(request, "Group Successfully Updated")
    else:
        form = Contact_GroupForm(instance=group)
    return render(request, 'contacts/group_update.html', {'form': form})


@login_required(login_url='/login/')
def group_delete(request, pk, template_name='contacts/confirm_group_delete.html'):
    group = get_object_or_404(Contact_Group, pk=pk)    
    if request.method=='POST':
        group.delete()
        messages.success(request, "Group Successfully Deleted")
        return redirect('group_list')
    return render(request, template_name, {'object':group})