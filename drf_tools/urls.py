"""drf_tools URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.routers import DefaultRouter

from book_api_swagger.viewsets import BookViewSet
from read_write_serializer_demo.viewsets import ReadWriteFieldViewSet
from tools.schemas.demo_api import get_demo_api, post_demo_api

router = DefaultRouter()
router.register(r"read_write_field", ReadWriteFieldViewSet)
router.register(r"book_api_swagger", BookViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r"^get_demo_api/", get_demo_api),
    url(r"^post_demo_api/", post_demo_api),
    url(r'^', include(router.urls)),
]

schema_view = get_schema_view(
    openapi.Info(
        title="DRF TOOLS API",
        default_version="v1",
    ),
    public=True,
)

urlpatterns += [
    url(r"^swagger(?P<format>\.json|\.yaml)$", schema_view.without_ui(cache_timeout=0), name="schema-json"),
    url(r"^swagger/$", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    url(r"^redoc/$", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]