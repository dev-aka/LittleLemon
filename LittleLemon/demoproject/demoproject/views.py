from rest_framework.decorators import permission_classes
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
#set permission_classes attribute
from .models import MenuItem
class MenuItemsView(generics.ListCreateAPIView):
   permission_classes = [IsAuthenticated]
   queryset = MenuItem.objects.all()
   serializer_class = MenuItemSerializer