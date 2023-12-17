from django.shortcuts import render
from rest_framework import viewsets
from . import models, serializers
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from . permissions import ReviewerOrReadOnly, AdminOrReadOnly
# Create your views here.



"""
This viewset automatically provides `list` and `retrieve` actions.
"""
class ProductViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticatedOrReadOnly] this is build in Danogo
    permission_classes = [AdminOrReadOnly]
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer


class ProductReviewViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    permission_classes = [ReviewerOrReadOnly]
    queryset = models.ProductReview.objects.all()
    serializer_class = serializers.ProductReviewSerializer
