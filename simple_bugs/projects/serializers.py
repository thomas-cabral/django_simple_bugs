from rest_framework import serializers

from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    group = serializers.Field('group.id')

    class Meta:
        model = Project
        fields = ('title', 'description', 'slug', 'group')