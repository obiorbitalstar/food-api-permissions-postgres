from rest_framework import serializers
from .models import Menu

class MenuSerializer(serializers.ModelSerializer):
    class Meta: 
        fields = ('id','dish_name','customer','price','description','ordered_at')
        model = Menu
        