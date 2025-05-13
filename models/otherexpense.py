from django.db import models

class OtherExpense(models.Model):
    description = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3)
    date = models.DateField()
    CURRENCY_CHOICES = [
    ("USD", "US Dollar"),
    ("EUR", "Euro"),
    ("GBP", "British Pound"),
    ("Ksh", "Kenya Shillings"),
    # Add other currencies as needed
]
currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES)

    def __str__(self):
    return f"Other Expense: {self.description} ({self.date})"
