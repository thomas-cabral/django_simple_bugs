from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.utils.encoding import python_2_unicode_compatible
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
    working_on = models.ManyToManyField(User, related_name='working_on', null=True, blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Requirement, self).save(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
        return 'simple_bugs:requirement_detail', (), {'pk': self.pk, 'slug': self.slug}


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
    assigned_to = models.ForeignKey(User, related_name='assigned', null=True, blank=True)
    requirement = models.ForeignKey(Requirement, related_name='requirement', null=True, blank=True,
                                    verbose_name='Related Requirement')

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Case, self).save(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
        return 'simple_bugs:case_detail', (), {'pk': self.pk, 'slug': self.slug}
