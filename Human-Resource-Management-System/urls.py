from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from employees import views

# Configuração do Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="HR Management API",
        default_version='v1',
        description="Documentation for HR Management API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@hr.local"),
        license=openapi.License(name="GNU GPL"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()
router.register(r'employees', views.EmployeeViewSet)
router.register(r'payrolls', views.PayrollViewSet)
router.register(r'benefits', views.BenefitViewSet)
router.register(r'performance_reviews', views.PerformanceReviewViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),

    # URLs do Swagger
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
]
