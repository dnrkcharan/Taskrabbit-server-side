from django.db import models

# Create your models here.
class Name(models.Model):
    name = models.CharField()

class Student(Name):
    student_branch = models.CharField()

class Professor(Name):
    teaching_strength = models.CharField()



class Expense(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, choices=get_currencies)


    class Meta:
        db_table = "expense"

