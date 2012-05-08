import django.dispatch

start_masquerading = django.dispatch.Signal(providing_args=['request'])
stop_masquerading = django.dispatch.Signal(providing_args=['request'])

