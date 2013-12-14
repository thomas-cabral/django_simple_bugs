from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Requirement(models.Model):
    #data fields
    title = models.CharField(max_length=55)
    detail = models.TextField()
    #date fields
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    # relationships
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return '/requirement/%i/' % self.id


class Bug(models.Model):
    #data fields
    title = models.CharField(max_length=55)
    detail = models.TextField()
    #date fields
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    #relationships
    user = models.ForeignKey(User)
    requirement = models.ForeignKey(Requirement, null=True, blank=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return '/bugs/%i/' % self.id