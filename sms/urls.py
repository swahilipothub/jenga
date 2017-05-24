from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/login/'}, name='logout'),
]

urlpatterns += [
	url(r'^contacts/', include('contacts.urls')),
]

urlpatterns += [
	url(r'^', include('sph_messages.urls')),
]