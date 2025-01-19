from django.db import models

class Account(models.Model):
    name = models.CharField(max_length=100)
    account_type = models.CharField(max_length=50)  # e.g., Asset, Liability, Equity, Revenue, Expense
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return self.name

class Transaction(models.Model):
    date = models.DateField()
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    account_debit = models.ForeignKey(Account, related_name='debit_transactions', on_delete=models.CASCADE)
    account_credit = models.ForeignKey(Account, related_name='credit_transactions', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.description} on {self.date}"
