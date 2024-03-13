from rest_framework import serializers
from .models import Project, Survey, Element

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"

class SurveySerializer(serializers.Serializer):
    class Meta:
        model = Survey
        fields = "__all__"

class ElementSerializer(serializers.Serializer):
    class Meta:
        model = Element
        fields = "__all__"
