from django.contrib import admin
from .models import Employee, Payroll, Benefit, PerformanceReview

admin.site.register(Employee)
admin.site.register(Payroll)
admin.site.register(Benefit)
admin.site.register(PerformanceReview)
