from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listing(models.Model):
    CATEGORIES = [
            ('Fashion', 'Fashion'),
            ('Toys', 'Toys'),
            ('Electronics', 'Electronics'),
            ('Home', 'Home'),
    ]
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=300)
    starting_bid = models.DecimalField(max_digits=7, decimal_places=2)
    url = models.CharField(max_length=300, blank=True)
    category = models.CharField(max_length=11, choices=CATEGORIES)

    def __str__(self):
        return f"Title: {self.title} \n Starting Bid: {self.starting_bid} \n URL {self.url}"

class Watchlist(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    pass
