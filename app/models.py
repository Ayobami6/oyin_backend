from django.db import models
from sparky_utils.decorators import str_meta
from django.utils import timezone
import uuid
from ckeditor.fields import RichTextField

# Create your models here.


@str_meta
class BannerText(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField(null=True, blank=True)


@str_meta
class AdvertBanner(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="ads/")


@str_meta
class ProductCategory(models.Model):
    name = models.CharField(max_length=100)


@str_meta
class Product(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True, primary_key=True
    )
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = RichTextField()
    views = models.IntegerField(default=0)
    category = models.ForeignKey(
        ProductCategory, on_delete=models.SET_NULL, null=True, blank=True
    )
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)


@str_meta
class ProductAssets(models.Model):
    name = models.CharField(max_length=100)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="product_assests/", null=True, blank=True)
    alt = models.CharField(max_length=100, null=True, blank=True)
