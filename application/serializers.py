from rest_framework import serializers

from .models import ApplicationModel


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationModel
        fields = ('id', 'name', 'key')
        read_only_fields = ['key']


class ApplicationKeySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationModel
        fields = ('id', 'name', 'key')
