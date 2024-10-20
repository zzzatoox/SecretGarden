from django.contrib import admin
from .models import Product, Category, SubCategory


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ("title",)


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "category")
    search_fields = ("title", "category__title")
    list_filter = ("category",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "category",
        "subcategory",
        "price",
        "sale_price",
        "is_available",
    )
    search_fields = ("title", "category__title", "subcategory__title")
    list_filter = ("category", "subcategory", "is_available")
    readonly_fields = ("slug", "created_at")
