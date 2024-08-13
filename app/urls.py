from django.urls import path
from .views import BannerTextAPIView

urlpatterns = [path("/banner", BannerTextAPIView.as_view(), name="banner")]
