from django.urls import path, include
from .views import (
    AdvertBannerAPIView,
    BannerTextAPIView,
    AllProductCategories,
    ProductAPIViewset,
)

from rest_framework import routers

router = routers.SimpleRouter(trailing_slash=False)

router.register(r"products", ProductAPIViewset, basename="products")

urlpatterns = [
    path("banner", BannerTextAPIView.as_view(), name="banner"),
    path("advert", AdvertBannerAPIView.as_view(), name="advert"),
    path("categories", AllProductCategories.as_view(), name="categories"),
    path("", include(router.urls)),
]
