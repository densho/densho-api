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
    title="DDR Explorer API",
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
    path(r'objects/<slug:object_id>/',
         views.object_detail, name='api-object'
    ),
    path(r'annotation/<slug:annotation_id>/',
         views.AnnotationDetail.as_view(), name='api-annotation'
    ),
    path(r'annotations/',
         views.Annotations.as_view(), name='api-annotations'
    ),
    path(r'objects/', views.objects, name='api-objects'),
    path(r'types/', views.types, name='api-types'),
    path('', views.api_index, name='api-index'),
]

urlpatterns = [
    # redirects
    path(r'verify-user/', views.verify_user),
    
    path(r'api/accounts/token/', views.CustomAuthToken.as_view()),
    path(r'api/accounts/', include('rest_registration.api.urls')),
    path(r'api/auth/', include('rest_framework.urls', namespace='rest_framework')),
    path(r'api/v1/', include(api_urlpatterns)),
    path(r'api/swagger<slug:format>\.json|\.yaml)',
         schema_view.without_ui(cache_timeout=0), name='schema-json'
    ),
    path(r'api/swagger/',
         schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'
    ),
    path('', views.index),
]
