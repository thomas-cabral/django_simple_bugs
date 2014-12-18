from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
# Create your models here.


class Comment(models.Model):
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)
    # Get model
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')


class Project(models.Model):
    title = models.CharField(max_length=55)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Requirement(models.Model):
    title = models.CharField(max_length=55)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User)

    comment = GenericRelation(Comment)


class Case(models.Model):
    title = models.CharField(max_length=55)
    detail = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User)

    master_case = models.ForeignKey('self', null=True, blank=True)
    related = models.ManyToManyField('self', null=True, blank=True)

    comment = GenericRelation(Comment)