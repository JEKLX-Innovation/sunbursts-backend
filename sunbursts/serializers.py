from rest_framework import serializers
from .models import Sunburst

class SunburstSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sunburst
        fields = "__all__"
