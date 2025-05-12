
from django.db import models
class Prediction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.SET_NULL, null=True)
    prediction_type = models.CharField(max_length=50)
    prediction_result = models.TextField()
    confidence_score = models.DecimalField(max_digits=5, decimal_places=2)
    prediction_date = models.DateTimeField()
