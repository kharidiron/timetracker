from django.views.generic import base
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Entry

import datetime
import calendar


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
                except:
                    return None
            else:
                try:
                    idx = [i for i, v in enumerate(months) if v[0] == arg][0]
                except:
                    return None
            return idx
    return months


class IndexView(base.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        return context


class RestrictedView(LoginRequiredMixin, base.TemplateView):
    template_name = 'restricted.html'

    def get_context_data(self, **kwargs):
        context = super(RestrictedView, self).get_context_data(**kwargs)

        return context


class YearView(base.TemplateView):
    template_name = 'year.html'

    def get_context_data(self, **kwargs):
        context = super(YearView, self).get_context_data(**kwargs)
        context['today'] = datetime.date.today()
        return context


class MonthView(base.TemplateView):
    template_name = 'month.html'

    def get_context_data(self, **kwargs):
        context = super(MonthView, self).get_context_data(**kwargs)
        context['today'] = datetime.date.today().strftime('%Y-%b-%d').split('-')
        context['month'] = context.get('month', context['today'][1])
        context['months'] = _months()[1:]
        context['daynames'] = calendar.weekheader(2).split(" ")
        context['days'] = calendar.monthcalendar(int(context['year']),
                                                 _months(context['month']))
        return context
