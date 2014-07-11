from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible
# Create your models here.


@python_2_unicode_compatible
class Group(models.Model):
    title = models.CharField(max_length=255)
    user = models.ManyToManyField(User, related_name='group_user_list')

    def __str__(self):
        return self.title