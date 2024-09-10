from django.urls import path
from .views import (
    EmployeeListCreate, EmployeeDetail,
    PayrollListCreate, PayrollDetail,
    BenefitListCreate, BenefitDetail,
    PerformanceReviewListCreate, PerformanceReviewDetail
)

urlpatterns = [
    # Employee URLs
    path('employees/', EmployeeListCreate.as_view(), name='employee-list-create'),
    path('employees/<int:pk>/', EmployeeDetail.as_view(), name='employee-detail'),

    # Payroll URLs
    path('payrolls/', PayrollListCreate.as_view(), name='payroll-list-create'),
    path('payrolls/<int:pk>/', PayrollDetail.as_view(), name='payroll-detail'),

    # Benefit URLs
    path('benefits/', BenefitListCreate.as_view(), name='benefit-list-create'),
    path('benefits/<int:pk>/', BenefitDetail.as_view(), name='benefit-detail'),

    # Performance Review URLs
    path('performance_reviews/', PerformanceReviewListCreate.as_view(), name='performance_review-list-create'),
    path('performance_reviews/<int:pk>/', PerformanceReviewDetail.as_view(), name='performance_review-detail'),
]
