from django.urls import path 
from .views import MenuList,MenuDetails

urlpatterns = [
    path('',MenuList.as_view(),name = 'menu'),
    path('<int:pk>/',MenuDetails.as_view(),name = 'menu_details')
]