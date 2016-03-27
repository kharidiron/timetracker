from django.conf.urls import url

from . import views

app_name = 'tracker'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<year>\d{4})/$', views.dates, name='yearly'),
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/$', views.dates, name='monthly'),
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>([0-9]|[1-9][0-9]))$', views.dates, name='daily'),
]
