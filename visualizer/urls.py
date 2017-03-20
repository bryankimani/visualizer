"""visualizer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from dashboard.views import index
from twittermine.views import get_tweets
from facebookmine.views import get_posts
from account.forms import RegistrationExtendedForm
from registration.backends.default.views import RegistrationView
from django.conf import settings
from django.conf.urls.static import static
import account.regbackend

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^tweets/$', get_tweets, name='tweets'),
    url(r'^posts/$', get_posts, name='posts'),
    url(r'^admin/', admin.site.urls),
    url(r'^profile/', include('account.urls')),
    # using my registration form to override the default
    url(r'^accounts/register/$', RegistrationView.as_view(form_class = RegistrationExtendedForm), name = 'create_account'),
    url(r'^accounts/', include('registration.backends.hmac.urls')),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
