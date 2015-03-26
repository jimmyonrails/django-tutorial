from django.conf.urls import patterns, include, url
from django.contrib import admin
from stores.views import store_list, store_detail
from pages.views import home

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lunch.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', home, name='home'),
    url(r'^store/', include('stores.urls')),
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
)
