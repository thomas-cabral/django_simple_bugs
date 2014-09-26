from rest_framework import serializers
from django.forms import widgets

from .models import Case, TestCase, TestStep


class TestCaseBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestCase
        fields = ('id', 'title')


class CaseSerializer(serializers.ModelSerializer):
    test_cases = TestCaseBaseSerializer(many=True)

    class Meta:
        model = Case
        fields = ('id', 'type', 'title', 'detail', 'test_cases', 'closed', 'slug', 'created_on', 'user')


class TestStepSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestStep
        fields = ('title', 'data')


class TestCaseSerializer(serializers.ModelSerializer):
    test_steps = TestStepSerializer()

    class Meta:
        model = TestCase
        fields = ('case', 'description', 'test_steps')
