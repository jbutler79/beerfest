from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.core.urlresolvers import reverse_lazy

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('lbtf.urls')),
    url(r'^login/$', auth_views.login,
        {'template_name': 'login.html'}, name='mysite_login'),
    url(r'^logout/$', auth_views.logout,
        {'next_page': reverse_lazy('index')}, name='mysite_logout'),


]
