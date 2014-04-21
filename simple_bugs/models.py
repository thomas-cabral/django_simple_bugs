from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.utils.encoding import python_2_unicode_compatible
from simple_history.models import HistoricalRecords
# Create your models here.


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
