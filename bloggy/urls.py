from django.conf.urls import patterns, include, url
from django.contrib import admin
from bloggy.views.base import login_user,main

urlpatterns = patterns('',
    # Examples:
		url(r'^login/$',login_user), 
    url(r'^$', login_user),
    url(r'^main/$', main),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
