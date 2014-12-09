from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from swampdragon.models import SelfPublishModel
from simple_comments.models import Comment


class Project(models.Model):
    title = models.CharField(max_length=55)
    created = models.DateTimeField()


class Requirement(models.Model):
    title = models.CharField(max_length=55)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)

    comment = GenericRelation(Comment)


class Case(models.Model):
    title = models.CharField(max_length=55)
    detail = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)

    master_case = models.ForeignKey('self', null=True, blank=True)

    comment = GenericRelation(Comment)