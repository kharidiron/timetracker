from django import forms

from .models import Entry


class TaskEntryForm(forms.ModelForm):
    start = forms.TimeInput(format='%H:%M')
    stop = forms.TimeInput(format='%H:%M')
    task = forms.CharField(max_length=200)

    class Meta:
        model = Entry
        fields = ['start', 'stop', 'task']
