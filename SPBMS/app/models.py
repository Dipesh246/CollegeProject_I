from django.db import models
from django.contrib.auth.models import AbstractUser,Group, Permission

class User(AbstractUser):
    profile_picture = models.ImageField(upload_to='profile_picture/', blank=True)
    registration_date = models.DateField(auto_now_add=True)
    phone_number = models.BigIntegerField(blank=True,null=True)
    groups = models.ManyToManyField(Group, related_name='app_users')
    user_permissions = models.ManyToManyField(Permission, related_name='app_users')

    def __str__(self) -> str:
        return self.username
    
class Budeget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    budget_name = models.CharField(max_length=100,default=None)
    monthly_income = models.DecimalField(max_digits=10,decimal_places=2)
    
    
    def __str__(self) -> str:
        return self.budget_name
    
class Category(models.Model):
    budget = models.ForeignKey(Budeget,on_delete=models.CASCADE)
    category_name = models.CharField(max_length=100)
    allocated_amount = models.DecimalField(max_digits=10,decimal_places=2)
    

    def __str__(self) -> str:
        return self.category_name
    
class Expense(models.Model):
    budget = models.ForeignKey(Budeget, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    remaining_amount = models.DecimalField(max_digits=10,decimal_places=2)
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    date = models.DateField()

#     def __str__(self) -> str:
#         return self.expense_name
    
# class Goal(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     goal_name = models.CharField(max_length=100)
#     target_amount = models.DecimalField(max_digits=10, decimal_places=2)
#     start_date = models.DateField()
#     end_date = models.DateField()

#     def __str__(self) -> str:
#         return self.goal_name
    
# class Saving(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     saving_name = models.CharField(max_length=100)
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     date = models.DateField()

#     def __str__(self):
#         return self.saving_name

# class Transaction(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     TYPE_CHOICES = (
#         ('income', 'Income'),
#         ('expense', 'Expense'),
#     )
#     type = models.CharField(max_length=10, choices=TYPE_CHOICES)
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     date = models.DateField()

#     def __str__(self):
#         return f'{self.type} - {self.amount}'
    
# class Reminder(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     title = models.CharField(max_length=100)
#     description = models.TextField()
#     date = models.DateField()
#     time = models.TimeField()

#     def __str__(self):
#         return self.title

