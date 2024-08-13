from rest_framework import serializers

from app.models import BannerText


class BannerTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = BannerText
        fields = "__all__"
