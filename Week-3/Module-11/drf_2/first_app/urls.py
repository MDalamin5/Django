from django.urls import path, include
from rest_framework import routers
from . views import ProductViewSet, ProductReviewViewSet


# Create a router and register our ViewSets with it.
router = routers.DefaultRouter()
router.register('products', ProductViewSet)
router.register('reviews', ProductReviewViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]