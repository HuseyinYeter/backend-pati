from rest_framework import serializers
from .models import *


class ReportSerializer(serializers.ModelSerializer):

    image = serializers.ImageField(required=True, use_url=True)

    class Meta:
        model = Report
        fields = '__all__'