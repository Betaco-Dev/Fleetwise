from django.db import models
from django.core.exceptions import ValidationError

class OtherExpense(models.Model):
    CURRENCY_CHOICES = [
        ("USD", "US Dollar"),
        ("EUR", "Euro"),
        ("GBP", "British Pound"),
        ("Ksh", "Kenyan Shilling"),
    ]

    CATEGORY_CHOICES = [
        ("fuel", "Fuel"),
        ("maintenance", "Maintenance"),
    ]

    description = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, null=True, blank=True)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        if self.amount < 0:
            raise ValidationError("Amount cannot be negative.")

    def __str__(self):
        return f"Other Expense: {self.description} ({self.date})"

    class Meta:
        verbose_name = "Other Expense"
        verbose_name_plural = "Other Expenses"
        indexes = [
            models.Index(fields=["date"]),
            models.Index(fields=["currency"]),
        ]
