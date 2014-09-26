from rest_framework import serializers

from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    cases = serializers.PrimaryKeyRelatedField(many=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'cases')