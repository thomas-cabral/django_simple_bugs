from django.db import models
from django.template.defaultfilters import slugify
from django.utils.encoding import python_2_unicode_compatible

from simple_bugs.groups.models import Group

# Create your models here.


@python_2_unicode_compatible
class Project(models.Model):
    title = models.CharField(max_length=55)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    group = models.ForeignKey(Group, related_name="project_group")

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Project, self).save(*args, **kwargs)

    def __str__(self):
        return self.title