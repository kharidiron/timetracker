from django.db import models
from django.contrib.auth.models import User


class UserData(models.Model):
    user = models.ForeignKey(User, editable=False)

    class Meta:
        abstract = True


class Entry(UserData):
    date = models.DateField('date')
    start = models.TimeField('start time')
    stop = models.TimeField('stop time')
    task = models.CharField('task', max_length=200)

    def __str__(self):
        return "<Entry: ({} {}-{}) {}>".format([self.date, self.start,
                                                self.stop, self.task])
