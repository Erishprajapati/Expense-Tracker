from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Transaction(models.Model):
    Transaction_Types = [
        ('Income', 'income'),
        ('Expenses', 'expenses')
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=20, choices = Transaction_Types, default = 'expenses')
    category = models.CharField(max_length=40)
    description = models.TextField()
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} made {self.amount} through {self.description} at {self.date}"
    


class Budget(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    monthly_limit = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.user} has {self.monthly_limit}"
    