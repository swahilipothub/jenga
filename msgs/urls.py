from django.conf.urls import url

from msgs import views

urlpatterns = [
	url(r'^history/', views.sms_list, name='sms_list'),
	url(r'^fetch/', views.sms_fetch, name='sms_fetch'),
	# url(r'^queue/', views.sms_queue, name='sms_queue'),
	url(r'^balance/', views.user_balance, name='user_balance'),
    url(r'^', views.sms_create, name='sms_create'),
]
