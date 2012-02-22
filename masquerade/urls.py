from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^mask/$', 'masquerade.views.mask', name='start_masquerading'),
    url(r'^unmask/$', 'masquerade.views.unmask', name='stop_masquerading'),
)
