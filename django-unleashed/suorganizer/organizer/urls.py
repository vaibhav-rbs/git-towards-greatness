from django.conf.urls import url

<<<<<<< HEAD
from .views import (
    startup_list, tag_detail, tag_list, startup_detail
)

urlpatterns = [
    url(r'^startup/$',
    startup_list,
    name='organizer_startup_list'),
    url(r'^startup/(?P<slug>[\w\-]+)/$',
    startup_detail,
    name='organizer_startup_detail'),
    url(r'^tag/$',
    tag_list,
    name='organizer_tag_list'),
    url(r'^tag/(?P<slug>[\w\-]+)/$',
    tag_detail,
    name='organizer_tag_detail'),
]
=======
from .views import homepage, tag_detail

urlpatterns = [
    url(r'^$', homepage),
    url(r'^tag/(?P<slug>[\w\-]+)/$',
    tag_detail,
    name='organizer_tag_detail')
]
>>>>>>> 00d1a2a71cd4a0887ab9b92b796cc9e9bf88ed16
