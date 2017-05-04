from django.conf.urls import url, include
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

from contacts import views

from django.contrib import admin

urlpatterns = [

	url(r'^admin/', admin.site.urls),

    url(r'^$', views.index, name='index'),\
]

urlpatterns += [
    url(r'^groups/$', views.group_list, name='group_list'),
    url(r'^groups/create/$', views.group_create, name='group_create'),
    url(r'^groups/(?P<pk>\d+)/update/$', views.group_update, name='group_update'),
]

urlpatterns += [
    url(r'^contacts/$', views.contact_list, name='contact_list'),
    url(r'^contacts/create/$', views.contact_create, name='contact_create'),
    # url(r'^books/(?P<pk>\d+)/update/$', views.book_update, name='book_update'),
    # url(r'^books/(?P<pk>\d+)/delete/$', views.book_delete, name='book_delete'),
    
]

