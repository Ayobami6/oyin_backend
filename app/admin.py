from django.contrib import admin
from .models import AdvertBanner, BannerText, Product, ProductAssets, ProductCategory

# Register your models here.


class ProductAssetsAdmin(admin.StackedInline):
    model = ProductAssets
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductAssetsAdmin]
    list_display = ("name", "price", "category")
    search_fields = ("name", "category")
    list_filter = ("category",)


admin.site.register(Product, ProductAdmin)
admin.site.register(AdvertBanner)
admin.site.register(BannerText)
admin.site.register(ProductCategory)
