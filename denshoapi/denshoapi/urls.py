"""denshoapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.urls import include, path, re_path

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

from . import views

API_DESCRIPTION = """
API DESCRIPTION TEXT GOES HERE.
"""

api_info = openapi.Info(
    title="Densho API",
    default_version='v1',
    description=API_DESCRIPTION,
    terms_of_service="http://ddr.densho.org/terms/",
    contact=openapi.Contact(email="info@densho.org"),
    license=openapi.License(name="License TBD"),
)
schema_view = get_schema_view(
    #api_info,
    url=settings.SWAGGER_BASE_URL,
    #patterns=
    #urlconf=
    public=True,
    #validators=['flex', 'ssv'],
    #generator_class=
    #authentication_classes=
    permission_classes=(permissions.AllowAny,),
)

api_urlpatterns = [
    path(r'swagger<slug:format>\.json|\.yaml)',
         schema_view.without_ui(cache_timeout=0), name='schema-json'
    ),
    path(r'swagger/',
         schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'
    ),
    path('', views.api_index, name='api-index'),
]

urlpatterns = [
    path('', views.index),
]
