from django.conf.urls import include, url
from django.contrib import admin
from speakers import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^manager$', views.manager, name='manager'),
    url(r'^speaker/(?P<uuid>.*)/flight/(?P<flight_id>[0-9]+)/$', views.speaker_flight, name='speaker_flight'),
    url(r'^speaker/(?P<uuid>.*)/flight/(?P<flight_id>[0-9]+)/(?P<decision>[a-z]+)/$', views.speaker_flight_decision, name='speaker_flight_decision'),
    url(r'^speaker/(?P<uuid>.*)/$', views.speaker, name='speaker'),
    url(r'^admin/', include(admin.site.urls)),
]
