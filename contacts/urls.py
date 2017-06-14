from django.conf.urls import url, include

from contacts import views


urlpatterns = [
    url(r'^groups/$', views.group_list, name='group_list'),
    url(r'^group-count/$', views.group_count, name='group_count'),
    url(r'^groups/add/$', views.group_create, name='group_create'),
    url(r'^groups/(?P<pk>\d+)/update/$', views.group_update, name='group_update'),
    url(r'^groups/(?P<pk>\d+)/delete/$', views.group_delete, name='group_delete'),
]

urlpatterns += [
	url(r'^import_sheet/$', views.import_sheet, name="import_sheet"),
    url(r'^search/$', views.search, name='search'),
]

urlpatterns += [
    url(r'^add/$', views.contact_create, name='contact_create'),
    url(r'^count/$', views.contact_count, name='contact_count'),
    url(r'^(?P<pk>\d+)/edit/$', views.contact_update, name='contact_update'),
    url(r'^delete/(?P<pk>\d+)/$', views.contact_delete, name='contact_delete'),
    url(r'^export/$', views.export_contact_csv, name='export_contact_csv'),
    url(r'^import/$', views.contact_upload, name='contact_upload'),
    url(r'^$', views.contact_list, name='contact_list'),   
]

