from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect

from .forms import TaskEntryForm
from .models import Entry

import datetime
import calendar
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta as delta

calendar.setfirstweekday(calendar.MONDAY)


def _months(arg=None):
    months = [('', ''), ('January', 'Jan'), ('February', 'Feb'),
              ('March', 'Mar'), ('April', 'Apr'), ('May', 'May'),
              ('June', 'Jun'), ('July', 'Jul'), ('August', 'Aug'),
              ('September', 'Sep'), ('October', 'Oct'), ('November', 'Nov'),
              ('December', 'Dec')]
    if arg:
        if arg.isdigit():
            return months[int(arg)]
        else:
            arg = arg.capitalize()
            if len(arg) == 3:
                try:
                    idx = [i for i, v in enumerate(months) if v[1] == arg][0]
                except IndexError:
                    return None
            else:
                try:
                    idx = [i for i, v in enumerate(months) if v[0] == arg][0]
                except IndexError:
                    return None
        return idx
    return months


class IndexView(generic.base.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        return context


class RestrictedView(LoginRequiredMixin, generic.base.TemplateView):
    template_name = 'restricted.html'

    def get_context_data(self, **kwargs):
        context = super(RestrictedView, self).get_context_data(**kwargs)

        return context


class MonthView(generic.base.TemplateView):
    template_name = 'month.html'

    def get_context_data(self, **kwargs):
        context = super(MonthView, self).get_context_data(**kwargs)
        context['today'] = datetime.date.today().strftime('%Y-%b-%d').split('-')
        context['month'] = context.get('month', context['today'][1])
        context['months'] = _months()[1:]
        context['daynames'] = calendar.weekheader(2).split(" ")
        context['days'] = calendar.monthcalendar(int(context['year']),
                                                 _months(context['month']))
        context['prev_year'] = int(context['year']) - 1
        context['next_year'] = int(context['year']) + 1

        view_date = '-'.join([context['year'], context['month']])
        prev_month = (parse(view_date) + delta(months=-1)).strftime('%Y/%b')
        next_month = (parse(view_date) + delta(months=+1)).strftime('%Y/%b')
        context['prev_month'] = prev_month
        context['next_month'] = next_month
        return context


class DayView(generic.list.ListView):
    model = Entry
    context_object_name = 'entries'
    template_name = 'day.html'

    def get_context_data(self, **kwargs):
        context = super(DayView, self).get_context_data(**kwargs)
        context['form'] = TaskEntryForm
        return context

    def post(self, request, *args, **kwargs):
        form = TaskEntryForm(request.POST)
        self.object_list = self.get_queryset()

        if form.is_valid():
            context = super(DayView, self).get_context_data(**kwargs)
            context['form'] = TaskEntryForm
            save_it = form.save(commit = False)
            save_it.user = self.request.user
            save_it.save()
            return redirect(request.META['HTTP_REFERER'])
        else:
            context = super(DayView, self).get_context_data(**kwargs)
            context['form'] = form
            return self.render_to_response(context=context)
