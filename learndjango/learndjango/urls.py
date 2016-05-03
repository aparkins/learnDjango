from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^graphs/', include('graphs.urls')),
    url(r'^spyfall/', include('spyfall.urls')),
]
