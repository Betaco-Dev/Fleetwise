from django.db import models

class MaintenancePrediction(models.Model):
    vehicle = models.ForeignKey('Vehicle', on_delete=models.CASCADE)
    predicted_maintenance_date = models.DateField()
    confidence_score = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Prediction for {self.vehicle}: {self.predicted_maintenance_date} (Confidence: {self.confidence_score})"
