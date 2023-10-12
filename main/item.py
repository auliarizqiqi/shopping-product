from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    date_added = models.DateField(auto_now_add=True)
    amount = models.IntegerField(default=1)
    price = models.IntegerField()
    description = models.TextField()
    size = models.CharField(max_length=255, default=" ")
    #image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    
    # def __str__(self):
    #     return self.name
