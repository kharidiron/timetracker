from django.conf.urls import url

from .views import IndexView, RestrictedView, MonthView, DayView

app_name = 'myapp'
urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^restricted$', RestrictedView.as_view(), name='restricted'),
    url(r'^(?P<year>\d{4})/$', MonthView.as_view(), name='year'),
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/$', MonthView.as_view(),
        name='month'),
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/'
        r'(?P<day>([1-9]|0[1-9]|[12][0-9]|3[01]))$',
        DayView.as_view(), name='day'),
]
