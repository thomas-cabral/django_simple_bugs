from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.utils.encoding import python_2_unicode_compatible
from simple_history.models import HistoricalRecords

from simple_bugs.projects.models import Project
from simple_bugs.requirements.models import Requirement


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
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    #relationships
    user = models.ForeignKey(User, related_name='case_user')
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
        return 'simple_bugs_cases:case_detail', (), {'pk': self.pk, 'slug': self.slug}

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Case, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class TestCase(models.Model):
    case = models.ForeignKey(Case, related_name='test_cases')
    title = models.CharField(max_length=55)
    description = models.TextField()

    def __str__(self):
        return self.title


class TestStep(models.Model):
    test_case = models.ForeignKey(TestCase, related_name='test_steps')
    title = models.CharField(max_length=55)
    data = models.TextField()

    def __str__(self):
        return self.title