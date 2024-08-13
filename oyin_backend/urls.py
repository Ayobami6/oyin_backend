"""
URL configuration for oyin_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from app.views import RootPage

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", RootPage.as_view(), name="root_page"),
    path("api/v1", include("app.urls")),
    # Add more URLs here
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = "Oyin Eccommerce Admin Page"
admin.site.site_title = "Oyin Eccommerce Admin Portal"
admin.site.index_title = "Welcome to Oyin Eccommerce Admin Portal"
