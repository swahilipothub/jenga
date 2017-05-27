from django.conf.urls import url, include

from contacts import views


urlpatterns = [
    url(r'^groups/$', views.group_list, name='group_list'),
    url(r'^groups/add/s$', views.group_create, name='group_create'),
    url(r'^groups/(?P<pk>\d+)/update/$', views.group_update, name='group_update'),
]

urlpatterns += [
    url(r'^add/$', views.contact_create, name='contact_create'),
    url(r'^(?P<pk>\d+)/edit/$', views.contact_update, name='contact_update'),
    # url(r'^(?P<pk>\d+)/delete/$', views.contacts_delete, name='contact_delete'),
    url(r'^$', views.contact_list, name='contact_list'),   
]

