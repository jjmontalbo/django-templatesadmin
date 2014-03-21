try:
    from django.conf.urls import patterns, url
except ImportError:
    from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'templatesadmin.views.listing', name='templatesadmin-overview'),
    url(r'^edit(?P<path>.*)/$', 'templatesadmin.views.modify', name='templatesadmin-edit'),
)
