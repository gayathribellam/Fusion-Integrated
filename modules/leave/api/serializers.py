from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import LeaveRequest, LeaveType


class LeaveTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveType
        fields = '__all__'


class LeaveRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveRequest
        fields = '__all__'

    def validate(self, data):
        if data['end_date'] < data['start_date']:
            raise ValidationError("End date cannot be before start date.")
        return data
