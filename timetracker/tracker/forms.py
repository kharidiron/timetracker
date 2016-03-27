from django import forms

from .models import Record


class PostTask(forms.ModelForm):
    start = forms.TimeField(input_formats=['%H:%M', '%I:%M%p', '%I:%M %p'],
                            widget=forms.TimeInput(
                                format='%I:%M %p',
                                attrs={'class': 'form-control input-small'}))

    stop = forms.TimeField(input_formats=['%H:%M', '%I:%M%p', '%I:%M %p'],
                           widget=forms.TimeInput(
                                format='%I:%M %p',
                                attrs={'class': 'form-control input-small'}))

    task = forms.CharField(widget=forms.TextInput(
                                attrs={'class': 'form-control'}))

    class Meta:
        model = Record
        exclude = ('date', 'user',)
