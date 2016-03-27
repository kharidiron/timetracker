from django.shortcuts import render

from django.http import HttpResponseRedirect, Http404
from django.views import generic

import datetime
import calendar

from .forms import PostTask
from .models import Record


class IndexView(generic.ListView):
    template_name = 'tracker/index.html'
    context_object_name = ''

    def get_queryset(self):
        return


def dates(request, year, month=None, day=None):
    today = datetime.datetime.today().date().strftime('%Y %b %d').split(" ")
    context = dict(today=today)

    months = {v: k for k, v in enumerate(calendar.month_abbr)}
    context['months'] = [month for month in calendar.month_name][1:]

    year = int(year)
    target = _validate_year(year)
    context['year'] = year

    if month:
        month = month.capitalize()
        target = _validate_month(month, months)
        context['month'] = month
        calendar.setfirstweekday(calendar.SUNDAY)
        context['daysofweek'] = calendar.weekheader(2).split(" ")
        context['days'] = calendar.monthcalendar(year, months[month])

    if day:
        day = int(day)
        target = _validate_day(day, year, months[month])
        context['day'] = day

        if request.method == 'POST':
            if request.POST.get('delete'):
                record_id = request.POST.get('delete')
                query = Record.objects.get(pk=record_id).delete()
                return HttpResponseRedirect(request.META.get('HTTP_REFERER',
                                                             '/'))
            elif request.POST.get('add'):
                form = PostTask(request.POST)
                if form.is_valid():
                    record = form.save(commit=False)
                    record.date = datetime.date(year, months[month], day)
                    record.user = 'kharidiron'
                    record.save()
                    return HttpResponseRedirect(request.META.get(
                        'HTTP_REFERER', '/'))
            else:
                # something wen't wrong. We shouldn't be here.
                raise Http404

        else:
            form = PostTask()
            context['form'] = form

            records = Record.objects.filter(date__year=year,
                                            date__month=months[month],
                                            date__day=day)\
                                    .order_by('start')
            context['records'] = records

    return render(request, target, context)


def _validate_year(year):
    if year not in range(1900, 2100):
        return 'tracker/silly.html'
    else:
        return 'tracker/yearly.html'


def _validate_month(month, months):
    if month not in months.keys():
        return 'tracker/silly.html'
    else:
        return 'tracker/monthly.html'


def _validate_day(day, year, month_number):
    if day not in range(1, calendar.monthrange(year, month_number)[1] + 1):
        return 'tracker/silly.html'
    else:
        return 'tracker/daily.html'
