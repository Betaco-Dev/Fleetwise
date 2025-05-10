from django.db import models

class OtherExpense(models.Model):
    description = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3)
    date = models.DateField()

    def __str__(self):
        return f"Other Expense {self.id}"
