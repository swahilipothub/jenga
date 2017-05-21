from django.conf.urls import url, include
from django.views.generic import TemplateView
# from django.contrib.auth import views as auth_views

from contacts import views

from django.contrib import admin

urlpatterns = [

	url(r'^admin/', admin.site.urls),
]

urlpatterns += [
    url(r'^groups/$', views.group_list, name='group_list'),
    url(r'^groups/create/$', views.group_create, name='group_create'),
    url(r'^groups/(?P<pk>\d+)/update/$', views.group_update, name='group_update'),
]

urlpatterns += [
    
    url(r'^create/$', views.contact_create, name='contact_create'),

    url(r'^(?P<pk>\d+)/update/$', views.contact_update, name='contact_update'),
    # url(r'^contacts/(?P<pk>\d+)/delete/$', views.contacts_delete, name='contact_delete'),

    url(r'^$', views.contact_list, name='contact_list'),
    
]

