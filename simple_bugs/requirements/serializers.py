from rest_framework import serializers
from django.forms import widgets

from simple_bugs.cases.models import Case
from .models import Requirement


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
