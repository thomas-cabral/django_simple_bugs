__author__ = 'Thomas'
from rest_framework import serializers
from django.forms import widgets

from simple_bugs.cases.models import Case
from simple_bugs.requirements.models import Requirement


class CaseSerializer(serializers.Serializer):
    class Meta:
        model = Case
        fields = ('pk', 'type', 'title', 'detail', 'closed', 'slug', 'created_on', 'user')

    pk = serializers.Field()
    type = serializers.ChoiceField(choices=Case.type_choice)
    title = serializers.CharField(max_length=55)
    detail = serializers.CharField(widget=widgets.Textarea, max_length=100000)
    closed = serializers.BooleanField(required=False)
    slug = serializers.SlugField(required=False)
    created_on = serializers.DateTimeField(required=False)
    user = serializers.Field(source='user.username')

    def restore_object(self, attrs, instance=None):
        if instance:
            instance.type = attrs.get('type', instance.type)
            instance.title = attrs.get('title', instance.title)
            instance.detail = attrs.get('detail', instance.detail)
            instance.closed = attrs.get('closed', instance.closed)
            return instance
        return Case(**attrs)


class RequirementSerializer(serializers.Serializer):
    class Meta:
        model = Requirement
        fields = ('pk', 'title', 'detail', 'slug', 'user', 'working_on')

    pk = serializers.Field()
    title = serializers.CharField(max_length=55)
    detail = serializers.CharField(widget=widgets.Textarea, max_length=100000)
    slug = serializers.SlugField(required=False)
    user = serializers.RelatedField()
    working_on = serializers.RelatedField(many=True)

    def restore_object(self, attrs, instance=None):
        if instance:
            instance.title = attrs.get('title', instance.title)
            instance.detail = attrs.get('detail', instance.detail)
            return instance
        return Case(**attrs)


from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    cases = serializers.PrimaryKeyRelatedField(many=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'cases')