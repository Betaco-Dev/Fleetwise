# Fleetwise/main/services/other_expense_utils.py

from ..models.other_expense import OtherExpense

def create_other_expense(data):
    expense = OtherExpense(**data)
    expense.full_clean()  # Triggers model validation, e.g., negative amounts
    expense.save()
    return expense

def update_other_expense(expense_id, data):
    expense = OtherExpense.objects.get(pk=expense_id)
    for key, value in data.items():
        setattr(expense, key, value)
    expense.full_clean()
    expense.save()
    return expense

def delete_other_expense(expense_id):
    expense = OtherExpense.objects.get(pk=expense_id)
    expense.delete()
