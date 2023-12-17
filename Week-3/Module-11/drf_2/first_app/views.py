from django.shortcuts import render
from rest_framework import viewsets
from . import models, serializers
# Create your views here.




class ProductViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer


class ProductReviewViewSet(viewsets.ModelViewSet):
    queryset = models.ProductReview.objects.all()
    serializer_class = serializers.ProductReviewSerializer
