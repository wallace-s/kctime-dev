from django.conf.urls import patterns, include, url
from django.contrib.auth.models import User

from django.contrib import admin
admin.autodiscover()

users = User.objects.all()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
	url(r'^timesheet/$', 'timesheetapp.views.index'),
	url(r'^login/$', 'django.contrib.auth.views.login',extra_context={'users':users}),
	url(r'^register/$', 'timesheetapp.views.register'),
	url(r'^logout/$', 'timesheetapp.views.logout_view'),
	url(r'^success/$', 'timesheetapp.views.sucess'),
)