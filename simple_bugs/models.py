from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
# Create your models here.


class Requirement(models.Model):
    #data fields
    title = models.CharField(max_length=55)
    detail = models.TextField()
    slug = models.SlugField(blank=True, null=True)
    #date fields
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    # relationships
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Requirement, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return '/requirement/%i/' % self.id


class Bug(models.Model):
    #data fields
    title = models.CharField(max_length=55)
    detail = models.TextField()
    slug = models.SlugField(blank=True, null=True)
    #date fields
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    #relationships
    user = models.ForeignKey(User)
    requirement = models.ForeignKey(Requirement, null=True, blank=True)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Bug, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return '/bugs/%i/' % self.id


class FeatureRequest(models.Model):
    #data fields
    title = models.CharField(max_length=55)
    detail = models.TextField()
    slug = models.SlugField(blank=True, null=True)
    #date fields
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    #relationships
    user = models.ForeignKey(User)
    requirement = models.ForeignKey(Requirement, null=True, blank=True)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(FeatureRequest, self).save(*args, **kwargs)