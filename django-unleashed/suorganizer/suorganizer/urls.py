from django.conf.urls import include, url
from django.contrib import admin

from organizer import urls as organizer_urls
from blog import urls as blog_urls
from .views import redirect_root

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/',include(blog_urls)),
    url(r'^$', redirect_root),
]
