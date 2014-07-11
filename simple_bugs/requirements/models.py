from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.utils.encoding import python_2_unicode_compatible
from simple_history.models import HistoricalRecords

from simple_bugs.projects.models import Project

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
    user = models.ForeignKey(User, related_name='requirements_user')
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
        return 'simple_bugs_requirements:requirement_detail', (), {'pk': self.pk, 'slug': self.slug}

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Requirement, self).save(*args, **kwargs)

    def __str__(self):
        return self.title