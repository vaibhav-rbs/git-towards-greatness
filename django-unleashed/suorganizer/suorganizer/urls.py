from django.conf.urls import include, url
from django.contrib import admin

from organizer import urls as organizer_urls
<<<<<<< HEAD
from blog import urls as blog_urls
from .views import redirect_root

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/',include(blog_urls)),
    url(r'^$', redirect_root),
=======

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include(organizer_urls)),
>>>>>>> 00d1a2a71cd4a0887ab9b92b796cc9e9bf88ed16
]
