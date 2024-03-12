from rest_framework import serializers
from .models import Project

class SunburstSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"
