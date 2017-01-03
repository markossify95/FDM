from django.conf.urls import url
from . import views

# PASSWORD: fonis2016

# /network/
urlpatterns = [
    url(r'^profiles/(?P<id>[0-9]+)/$', views.profile_view),
    # url(r'^profiles/new/(?P<id>[0-9]+)/$', views.profile_view),
    url(r'^search/$', views.filter_view),
    url(r'^login/$', views.login_view),
    url(r'^logout/$', views.logout_view),
]
