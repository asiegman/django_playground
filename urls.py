from django.conf.urls.defaults import *

# Enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^beta_alexsiegman_com/', include('beta_alexsiegman_com.foo.urls')),

    # Enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Enable the admin:
    (r'^admin/', include(admin.site.urls)),

    # Views for Polls
    (r'^polls/', include('polls.urls')),
)
