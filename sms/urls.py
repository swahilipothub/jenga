from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('contacts.urls')),
    # url(r'^contacts/', include('contacts.url')),
]
