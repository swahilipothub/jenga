import csv
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect

from .models import Contact, Contact_Group
from .forms import ContactForm, Contact_GroupForm, UploadFileForm

from django.contrib.postgres.search import SearchVector

from django.http import HttpResponseBadRequest, HttpResponse
# from _compact import JsonResponse
# import django_excel as excel

# Contact list.
@login_required(login_url='/login/')
def contact_list(request):
    contacts = Contact.objects.filter(user=request.user).order_by('-created')
    return render(request, 'contacts/contacts.html', {'contacts': contacts})

@login_required(login_url='/login/')
def contact_count(request):
    contact_count = Contact.objects.filter(user=request.user).count()
    return render(request, 'contacts/contact_count.html', {'contact_count': contact_count})


@login_required(login_url='/login/')
def contact_create(request):
    if request.method == 'POST':
        form = ContactForm(request.user, request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            mobile = form.cleaned_data['mobile']
            category = form.cleaned_data['category']

            contact_create = form.save(commit=False)
            contact_create.user = request.user
            contact_create.save()

            form = ContactForm(request.user)
            messages.success(request, "Contact Successfully Created")
    else:
        form = ContactForm(request.user)
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
        form = ContactForm(request.user, request.POST, instance=contact)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            mobile = form.cleaned_data['mobile']
            category = form.cleaned_data['category']

            contact_update = form.save(commit=False)
            contact_update.user = request.user
            contact_update.save()

            messages.success(request, "Contact Successfully Updated")
    else:
        form = ContactForm(request.user, instance=contact)
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

@login_required
def group_count(request):
    group_count = Contact_Group.objects.filter(user=request.user).count()
    return render(request, 'contacts/group_count.html', {'group_count': group_count})


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


@login_required(login_url='/login/')
def import_sheet(request):
    if request.method == "POST":
        form = UploadFileForm(request.user, request.POST, request.FILES)
        if form.is_valid():
            import_sheet = request.FILES['file'].save_to_database(
                            model=Contact,
                            mapdict=['first_name', 'last_name', 'mobile', 'id_number', 'category'],
                            commit=False)
            import_sheet.user = request.user
            import_sheet.save_to_database()
            return HttpResponse("OK")
        else:
            return HttpResponseBadRequest("Bad Request")
    else:
        form = UploadFileForm()
    return render(request, 'contacts/upload_form.html', {'form': form})


@login_required
def export_contact_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="contacts.csv"'
    writer = csv.writer(response)
    writer.writerow(['First name', 'Last name', 'Email address', 'Mobile Number', 'Group' ])
    contacts = Contact.objects.filter(user=request.user).values_list(
        'first_name', 'last_name', 'email', 'mobile', 'category_id')
    for contact in contacts:
        writer.writerow(contact)
    return response


@login_required
def search(request):
    item = request.GET['q']
    search =  Contact.objects.annotate(search=SearchVector(
        'first_name', 'last_name', 'mobile', 'email')).filter(search=item)
    return render(request, 'contacts/contact_search.html', {'object':search})