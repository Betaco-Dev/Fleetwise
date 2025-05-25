from rest_framework import serializers
from Fleetwise.main.models import analytics_report

class AnalyticsReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = analytics_report
        fields = ['id', 'report_name', 'created_date', 'data']
