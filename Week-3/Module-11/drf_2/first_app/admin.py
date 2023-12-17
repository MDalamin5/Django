from django.contrib import admin
from .models import Product, ProductReview

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')  # Fields to display in the admin panel
    search_fields = ('name',)  # Fields to search
    # Add any other admin configurations as needed

@admin.register(ProductReview)
class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'rating', 'created_at', 'update_at')  # Fields to display in the admin panel
    list_filter = ('product', 'rating')  # Add filters to the admin panel
    search_fields = ('user__username', 'product__name')  # Fields to search
    # Add any other admin configurations as needed
