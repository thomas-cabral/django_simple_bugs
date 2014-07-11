from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible

from simple_bugs.cases.models import Case



@python_2_unicode_compatible
class Estimate(models.Model):
    estimate_type = (
        ('ENGINEERING', 'Engineering'),
        ('PRODUCTION_QA', 'Production QA'),
    )
    type = models.CharField(choices=estimate_type, max_length=55)
    estimate = models.PositiveIntegerField(null=True, blank=True)
    total_time = models.PositiveIntegerField(null=True, blank=True)

    user = models.ForeignKey(User, related_name='estimate_user')
    case = models.ForeignKey(Case, related_name="case_estimate")

    @property
    def estimate_formatted(self):
        #for simplicity, assuming duration is int
        hours = self.estimate / 60

        minutes = self.estimate % 60
        return "%d hour %s minutes" % (hours, minutes)

    @property
    def total_formatted(self):
        #for simplicity, assuming duration is int
        hours = self.total_time / 60

        minutes = self.total_time % 60
        return "%d hour %s minutes" % (hours, minutes)

    @property
    def remaining_time(self):
        if self.total_time:
            remaining = self.estimate - self.total_time
        else:
            remaining = self.estimate

        hours = remaining / 60

        minutes = remaining % 60
        return '%d:%s:00' % (hours, minutes)

    @property
    def progress(self):
        if self.total_time:
            remaining = 100 * float(self.total_time) / float(self.estimate)
        else:
            remaining = 0

        return remaining

    def __str__(self):
        return '%s: %sm' % (self.type, self.estimate)
