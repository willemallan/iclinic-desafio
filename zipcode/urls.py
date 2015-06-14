from django.conf.urls import patterns, url

urlpatterns = patterns('zipcode.views',
    url(r'^$', 'zipcode_list'),
    url(r'^(?P<zip_code>[0-9]+)/$', 'zipcode_detail'),
)