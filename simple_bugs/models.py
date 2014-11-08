from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=55)


class Requirement(models.Model):
    title = models.CharField(max_length=55)


class Case(models.Model):
    title = models.CharField(max_length=55)