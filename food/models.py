from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

class Menu(models.Model):
    dish_name = models.CharField(max_length=64)
    customer = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    price = models.IntegerField()
    description = models.TextField()
    ordered_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.dish_name
    
    