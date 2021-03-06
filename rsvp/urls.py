"""rsvp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin

from rsvp.views import EventListView, RsvpCreateView, RsvpListView

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', EventListView.as_view(), name='events'),
    url(r'^rsvps/$', EventListView.as_view(), name='rsvps'),
    
    url(r'^rsvp/(?P<event_id>\d+)/$', RsvpCreateView.as_view(), name='rsvp'),
    url(r'^rsvps/(?P<event_id>\d+)/$', RsvpListView.as_view(), name='rsvps'),
]
