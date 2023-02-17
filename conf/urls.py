
import debug_toolbar
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.generic import TemplateView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

admin.site.site_header = 'AUTH Admin'
admin.site.index_title = 'Admin'

schema_view = get_schema_view(
    openapi.Info(
        title="AUTH API",
        default_version='v1',
        description="Auth 🚀  API Documentation",
        terms_of_service="https://www.auth.com/terms",
        contact=openapi.Contact(email="@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('',TemplateView.as_view(template_name='core/index.html')),
    path('admin/', admin.site.urls),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('__debug__/', include(debug_toolbar.urls)),
    path('health/', include('health_check.urls')),

    path('api/v1/',include('apps.core.urls')),
    path('api/v1/',include('apps.accounts.urls')),

]
