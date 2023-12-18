from django.shortcuts import render
from rest_framework import viewsets
from . import models, serializers
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from . permissions import ReviewerOrReadOnly, AdminOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
# Create your views here.



"""
This viewset automatically provides `list` and `retrieve` actions.
"""
class ProductViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticatedOrReadOnly] this is build in Danogo
    permission_classes = [AdminOrReadOnly]
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    # filter_backends = [filters.SearchFilter] # line20,21 if for searching
    # search_fields = ['name', 'description']

    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['price']


class ProductReviewViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    permission_classes = [ReviewerOrReadOnly]
    queryset = models.ProductReview.objects.all()
    serializer_class = serializers.ProductReviewSerializer


    #quick process
    filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['user__username'] # filter by username
    filterset_fields = ['rating', 'product'] # filter by product name and rating

    # reviews ordering
    # filter_backends = [filters.OrderingFilter]
    # ordering_fields = ['rating']

    # def get_queryset(self):  so long prcess
    #     """
    #     Optionally restricts the returned purchases to a given user,
    #     by filtering against a `username` query parameter in the URL.
    #     """
    #     queryset = models.ProductReview.objects.all()
    #     username = self.request.query_params.get('username')
    #     if username is not None:
    #         queryset = queryset.filter(user__username__icontains=username)
    #     return queryset
