from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.utils.encoding import python_2_unicode_compatible
from simple_history.models import HistoricalRecords
# Create your models here.


@python_2_unicode_compatible
class Project(models.Model):
    title = models.CharField(max_length=55)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Project, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class Requirement(models.Model):
    #data fields
    title = models.CharField(max_length=55)
    detail = models.TextField()
    slug = models.SlugField(blank=True, null=True)
    #date fields
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    # relationships
    user = models.ForeignKey(User, related_name='user')
    changed_by = models.ForeignKey(User, related_name='requirement_changed_by', null=True, blank=True)
    working_on = models.ManyToManyField(User, related_name='working_on', null=True, blank=True)
    project = models.ForeignKey(Project, related_name='requirement_project')
    #history
    history = HistoricalRecords()

    class Meta:
        ordering = ['-created_on']

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    @models.permalink
    def get_absolute_url(self):
        return 'simple_bugs:requirement_detail', (), {'pk': self.pk, 'slug': self.slug}

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Requirement, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class Case(models.Model):
    type_choice = (
        ('BUG', 'Bug'),
        ('FEATURE_REQUEST', 'Feature Request'),
    )
    #data fields
    type = models.CharField(max_length=155, choices=type_choice, default='BUG')
    title = models.CharField(max_length=55)
    detail = models.TextField()
    closed = models.BooleanField()
    slug = models.SlugField(blank=True, null=True)
    #date fields
    time_estimate = models.TimeField(null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    #relationships
    user = models.ForeignKey(User, related_name='created_by')
    changed_by = models.ForeignKey(User, related_name='case_changed_by', null=True, blank=True)
    assigned_to = models.ForeignKey(User, related_name='assigned', null=True, blank=True)
    requirement = models.ForeignKey(Requirement, related_name='requirement', null=True, blank=True,
                                    verbose_name='Related Requirement')
    project = models.ForeignKey(Project, related_name='case_project')
    #history
    history = HistoricalRecords()

    class Meta:
        ordering = ['-created_on']

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    @models.permalink
    def get_absolute_url(self):
        return 'simple_bugs:case_detail', (), {'pk': self.pk, 'slug': self.slug}

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Case, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


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
        return '%d hour %s minutes' % (hours, minutes)

    @property
    def progress(self):
        if self.total_time:
            remaining = 100 * float(self.total_time) / float(self.estimate)
        else:
            remaining = 0

        return remaining

    def __str__(self):
        return '%s: %sm' % (self.type, self.estimate)

