"""
Definition of urls for PASSweb.
"""

from datetime import datetime
from django.conf.urls import url
from django.views.generic import RedirectView
import django.contrib.auth.views

import app.forms
import app.views
import web.views

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    #url(r'^$', app.views.home, name='home'),
    #url(r'^contact$', app.views.contact, name='contact'),
    #url(r'^about', app.views.about, name='about'),
    #url(r'^login/$',
    #    django.contrib.auth.views.login,
    #    {
    #        'template_name': 'app/login.html',
    #        'authentication_form': app.forms.BootstrapAuthenticationForm,
    #        'extra_context':
    #        {
    #            'title': 'Log in',
    #            'year': datetime.now().year,
    #        }
    #    },
    #    name='login'),
    #url(r'^logout$',
    #    django.contrib.auth.views.logout,
    #    {
    #        'next_page': '/',
    #    },
    #    name='logout'),
    
    url(r'^$', RedirectView.as_view(url='/send_broadcast'), name='home'),
    url(r'^send_broadcast$', web.views.send_broadcast, name='send_broadcast'),
    url(r'^send_selective$', web.views.send_selective, name='send_selective'),
    url(r'^send_direct$', web.views.send_direct, name='send_direct')

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]
