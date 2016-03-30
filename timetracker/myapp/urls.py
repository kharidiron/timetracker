from django.conf.urls import url

from .views import IndexView, RestrictedView, MonthView


app_name = 'myapp'
urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^restricted$', RestrictedView.as_view(), name='restricted'),
    url(r'^(?P<year>\d{4})/$', MonthView.as_view(), name='year'),
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/$', MonthView.as_view(),
        name='month'),
    # url(r'^(?P<year>\d{4})/$', views.dates, name='yearly'),
    # url(r'^(?P<year>\d{4})/(?P<month>\w{3})/$', views.dates, name='monthly'),
    # url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>([0-9]|[1-9][0-9]))$', views.dates, name='daily'),
]
