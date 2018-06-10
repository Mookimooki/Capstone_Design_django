from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Fish, Report

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ('image_id', 'report_type', 'content', 'title')

class FishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fish
        fields = ('image','id')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
