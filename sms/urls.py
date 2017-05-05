from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('contacts.urls')),
    # url(r'^contacts/', include('contacts.url')),

    url(r'^login/$', auth_views.login,
        {'template_name': 'login.html'}, name='login'),

    url(r'^logout/$', auth_views.logout,
        {'next_page': '/login/'}, name='logout'),
]

#Add Django site authentication urls (for login, logout, password management)
# urlpatterns += [
#     url('^accounts/', include('django.contrib.auth.urls')),
# ]
