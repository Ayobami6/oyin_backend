from rest_framework import serializers

from app.models import AdvertBanner, BannerText, Product, ProductAssets, ProductCategory


class BannerTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = BannerText
        fields = "__all__"


class AdvertBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvertBanner
        fields = "__all__"


class ProductAssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductAssets
        fields = ("name", "image", "alt")


class ProductSerializer(serializers.ModelSerializer):
    assets = ProductAssetSerializer(many=True, read_only=True)
    groups_link = serializers.SerializerMethodField()
    self_link = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = "__all__"

    def get_groups_link(self, obj):
        request = self.context.get("request")
        base_url = request.build_absolute_uri("/")[:-1]
        url = f"{base_url}/products"
        return url

    def get_self_link(self, obj):
        request = self.context.get("request")
        base_url = request.build_absolute_uri("/")[:-1]
        url = f"{base_url}/products/{obj.id}"
        return url


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = "__all__"
