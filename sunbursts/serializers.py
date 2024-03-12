from rest_framework import serializers
from .models import Project, Survey

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"

class SurveySerializer(serializers.Serializer):
    class Meta:
        model = Survey
        fields = "__all__"
