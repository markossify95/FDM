from django.conf.urls import url
from . import views

# PASSWORD: fonis2016

# /network/
urlpatterns = [
    url(r'^profiles/(?P<id>[0-9]+)/$', views.profile_view),
]
