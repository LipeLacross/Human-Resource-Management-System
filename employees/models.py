from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    hire_date = models.DateField()
    job_title = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Payroll(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    pay_date = models.DateField()
    gross_pay = models.DecimalField(max_digits=10, decimal_places=2)
    deductions = models.DecimalField(max_digits=10, decimal_places=2)
    net_pay = models.DecimalField(max_digits=10, decimal_places=2)

class Benefit(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    benefit_type = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

class PerformanceReview(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    review_date = models.DateField()
    rating = models.IntegerField()
    comments = models.TextField()
