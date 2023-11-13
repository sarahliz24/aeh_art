from django.db import models
from profiles.models import UserProfile
from products.models import Product


class Wishlist(models.Model):
    ''' Model to display user wishlist'''

    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"WishList ({self.user})"
