from django.conf.urls import url

from sph_messages import views


urlpatterns = [
	url(r'^settings/add/', views.sms_settings_add, name="sms_settings_add"),
	url(r'^settings/(?P<pk>\d+)/edit/$', views.sms_settings_update, name='sms_settings_update'),
	url(r'^settings/', views.sms_settings_list, name="sms_settings_list"),
]

urlpatterns += [
	url(r'^history/', views.sms_list, name='sms_list'),
	url(r'^fetch/', views.sms_fetch, name='sms_fetch'),
	# url(r'^queue/', views.sms_queue, name='sms_queue'),
	url(r'^balance/', views.user_balance, name='user_balance'),
    url(r'^', views.sms_create, name='sms_create'),
]
