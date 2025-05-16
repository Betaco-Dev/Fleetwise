from django.db import models

class Currency(models.Model):
    currency_code = models.CharField(max_length=3, primary_key=True)
    currency_name = models.CharField(max_length=50)

    def __str__(self):
        return self.currency_name
