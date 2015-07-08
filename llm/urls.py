from django.conf.urls import include, url
from django.contrib import admin
from speakers import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^speaker/(?P<uuid>[^/]+)/$', views.speaker, name='speaker'),
    url(r'^admin/', include(admin.site.urls)),
]
