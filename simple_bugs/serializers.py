from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Case, Requirement, Project, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'content_type', 'object_id', 'body', 'user')


class CommentSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'body', 'user')


class CaseSerializer(serializers.ModelSerializer):
    comment = CommentSimpleSerializer(many=True, read_only=True)

    class Meta:
        model = Case
        fields = ('id', 'title', 'detail', 'user', 'master_case', 'comment')


class RequirementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requirement
        fields = ('id', 'title', 'user')


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'title')