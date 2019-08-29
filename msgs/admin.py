from django.contrib import admin
from msgs.models import Sms

# admin.site.register(Sms)

@admin.register(Sms)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('number', 'message', 'category', 'status', 'cost')
    search_fields = ('number', 'status')