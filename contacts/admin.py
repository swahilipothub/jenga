from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from contacts.models import Contact_Group, Contact


@admin.register(Contact_Group)
class ContactGroupAdmin(ImportExportModelAdmin):
    list_display = ('name', )

# class ContactInstanceInline(admin.TabularInline):
#     model = Contact

@admin.register(Contact)
class ContactAdmin(ImportExportModelAdmin):
    list_display = ('full_name', 'mobile',)
    search_fields = ('full_name', 'mobile',)
    # inlines = [ContactInstanceInline]