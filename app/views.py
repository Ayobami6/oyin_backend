from django.shortcuts import render
from rest_framework.views import APIView
from sparky_utils.response import service_response
from sparky_utils.exceptions import handle_internal_server_exception

from app.models import BannerText
from app.serializers import BannerTextSerializer

# Create your views here.


class RootPage(APIView):
    """API Root Page."""

    def get(self, request, format=None):
        return service_response(
            status=200,
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
                status=200,
                message="Banner Text retrieved successfully",
                data=serializer.data,
            )
        except Exception:
            return handle_internal_server_exception()
