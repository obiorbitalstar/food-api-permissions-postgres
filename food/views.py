from django.shortcuts import render
from rest_framework import generics

from .models import Menu
from .serializer import MenuSerializer
from .permissions import IsAuthorOrReadOnly
# Create your views here.

class MenuList(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class MenuDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permissions_classes = (IsAuthorOrReadOnly,)
