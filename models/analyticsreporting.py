from django.db import models

class AnalyticsReport(models.Model):
    report_name = models.CharField(max_length=100)
    created_date = models.DateField()
    data = models.BinaryField()

    def __str__(self):
        return self.report_name
