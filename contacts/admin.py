from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(ImportExportModelAdmin):
    pass