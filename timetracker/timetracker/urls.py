from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url('^', include('django.contrib.auth.urls')),
    url(r'^myapp/', include('myapp.urls')),
    url(r'^tracker/', include('tracker.urls')),
    url(r'^admin/', admin.site.urls),
]
