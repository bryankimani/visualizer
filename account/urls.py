from django.conf.urls import url
from account.views import profile

urlpatterns = [
    url(r'^edit/(?P<username>[\w\-]+)/$', profile, name='editprofile'),
]