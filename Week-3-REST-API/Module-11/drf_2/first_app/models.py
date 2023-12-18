from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length = 200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)  # 102.02
    def __str__(self) -> str:
        return self.name
    
class ProductReview(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE, related_name = 'reviews')
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1,6)])
    review = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) # when user create new review
    update_at = models.DateTimeField(auto_now=True) # when user edid his review
    class Meta:
        unique_together = ('product', 'user') # one user can give review only one

    def __str__(self) -> str:
        return f"{self.user.username} -- {self.product.name} -- Rating: {self.rating}"
