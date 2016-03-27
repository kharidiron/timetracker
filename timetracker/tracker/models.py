from django.db import models


class Record(models.Model):
    date = models.DateField('date')
    start = models.TimeField('start time')
    stop = models.TimeField('stop time')
    user = models.CharField('user', max_length=200)
    task = models.CharField('task', max_length=200)

    def __str__(self):
        return self.date, self.start, self.stop, self.user, self.task
