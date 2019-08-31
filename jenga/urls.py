from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.contrib import admin

from . import views 
from accounts import views as core_views


urlpatterns = [
    url(r'^login/$', core_views.login_view, name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(),
        {'next_page': '/login/'}, name='logout'),
    url(r'^signup/$', core_views.signup, name='signup'),
    url(r'^account_activation_sent/$', core_views.account_activation_sent,
        name='account_activation_sent'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        core_views.activate, name='activate'),
    url(r'^profile/$', core_views.profile, name='profile'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    # url(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
    # url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    url(r'^admin/', admin.site.urls),
]

urlpatterns += [
    url(r'^contacts/', include('contacts.urls')),
]

urlpatterns += [
    url(r'^', include('msgs.urls')),
]
