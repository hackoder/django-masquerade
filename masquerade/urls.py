from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^mask/$', 'masquerade.views.mask'),
    url(r'^unmask/$', 'masquerade.views.unmask'),
)
