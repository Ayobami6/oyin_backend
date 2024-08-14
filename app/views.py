from urllib import response
from django.shortcuts import render
from rest_framework.views import APIView
from sparky_utils.response import service_response
from sparky_utils.exceptions import handle_internal_server_exception
from typing import Any, List
from app.models import AdvertBanner, BannerText, Product, ProductAssets, ProductCategory
from app.serializers import (
    AdvertBannerSerializer,
    BannerTextSerializer,
    CategorySerializer,
    ProductSerializer,
)
from django.db.models import Q, Prefetch

from rest_framework import viewsets

# Create your views here.


class RootPage(APIView):
    """API Root Page."""

    def get(self, request, format=None):
        return service_response(
            status="success",
            message="Welcome to Oyin's Eccommerce API",
            data={},
        )


class BannerTextAPIView(APIView):
    """API for retrieving Banner Text."""

    serializer_class = BannerTextSerializer

    def get(self, request, *args, **kwargs):
        """Get handler to retrieve Banner Text"""
        try:
            # get the BannerText
            banner = BannerText.objects.all().first()
            # serialize the BannerText
            serializer = self.serializer_class(banner)
            # return the serialized BannerText
            return service_response(
                status="success",
                message="Banner Text retrieved successfully",
                data=serializer.data,
                status_code=200,
            )
        except Exception:
            return handle_internal_server_exception()


class AdvertBannerAPIView(APIView):
    """Banner api view"""

    def get(self, request, *args, **kwargs) -> Any:
        try:
            # get all advert banners
            banners = AdvertBanner.objects.all().order_by("-updated_at")[:5]
            serializer = AdvertBannerSerializer(banners, many=True)
            return service_response(
                status="success",
                message="Advert banners retrieved successfully",
                data=serializer.data,
                status_code=200,
            )

        except Exception:
            return handle_internal_server_exception()


class AllProductCategories(APIView):
    """API for retrieving all product categories."""

    def get(self, request, *args, **kwargs) -> Any:
        try:
            # get all product categories
            categories = ProductCategory.objects.all()
            # serialize the product categories
            serializer = CategorySerializer(categories, many=True)
            # return the serialized product categories
            return service_response(
                status="success",
                message="Product categories retrieved successfully",
                data=serializer.data,
                status_code=200,
            )
        except Exception:
            return handle_internal_server_exception()


class ProductAPIViewset(viewsets.ModelViewSet):
    """List all products"""

    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def list(self, request, *args, **kwargs) -> Any:
        """Product list get handler"""
        try:
            assets_fields: List[str] = ["name", "image", "alt"]
            # get query
            query = request.GET.get("search")
            category = request.GET.get("category")
            products = Product.objects.prefetch_related(
                Prefetch("assets", queryset=ProductAssets.objects.only(*assets_fields))
            ).all()
            if query:
                # search for products by name or description
                products = Product.objects.prefetch_related(
                    Prefetch(
                        "assets", queryset=ProductAssets.objects.only(*assets_fields)
                    )
                ).filter(Q(name__icontains=query) | Q(description__icontains=query))
            if category:
                # filter products by category
                products = Product.objects.prefetch_related(
                    Prefetch(
                        "assets", queryset=ProductAssets.objects.only(*assets_fields)
                    )
                ).filter(category=int(category))
            serializer = self.serializer_class(products, context={"request": request}, many=True)
            data = serializer.data
            return service_response(
                status="success",
                message="Products retrieved successfully",
                data=data,
                status_code=200,
            )

        except Exception:
            return handle_internal_server_exception()

    def retrieve(self, request, *args, **kwargs):
        """Product retrieve get handler"""
        try:
            assets_fields: List[str] = ["name", "image", "alt"]
            # get product
            product = self.get_object()
            # get product assets
            assets = ProductAssets.objects.only(*assets_fields).filter(product=product)
            serializer = ProductSerializer(product, context={"assets": assets})
            return service_response(
                status="success",
                message="Product retrieved successfully",
                data=serializer.data,
                status_code=200,
            )
        except Exception:
            return handle_internal_server_exception()
