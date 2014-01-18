__author__ = 'Thomas'
from rest_framework import serializers
from django.forms import widgets
from .models import Case


class CaseSerializer(serializers.Serializer):
    class Meta:
        model = Case
        fields = ('pk', 'type', 'title', 'detail', 'closed', 'user')

    pk = serializers.Field()
    type = serializers.ChoiceField(choices=Case.type_choice)
    title = serializers.CharField(max_length=55)
    detail = serializers.CharField(widget=widgets.Textarea, max_length=100000)
    closed = serializers.BooleanField(required=False)
    user = serializers.Field(source='user.username')

    def restore_object(self, attrs, instance=None):
        if instance:
            instance.type = attrs.get('type', instance.type)
            instance.title = attrs.get('title', instance.title)
            instance.detail = attrs.get('detail', instance.detail)
            instance.closed = attrs.get('closed', instance.closed)
            return instance
        return Case(**attrs)


from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    cases = serializers.PrimaryKeyRelatedField(many=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'cases')