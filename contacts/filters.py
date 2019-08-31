from django import forms
from .models import Contact, Contact_Group
import django_filters

class ContactFilter(django_filters.FilterSet):
    full_name = django_filters.CharFilter(lookup_expr='icontains')
    groups = django_filters.ModelMultipleChoiceFilter(queryset=Contact_Group.objects.all(),
        widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Contact
        fields = ['full_name', 'mobile', 'groups']