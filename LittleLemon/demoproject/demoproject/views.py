from rest_framework.decorators import permission_classes
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from LittleLemon.restaurant.models import MenuItem
from LittleLemon.restaurant.serializers import MenuItemSerializer
#set permission_classes attribute

class MenuItemsView(generics.ListCreateAPIView):
   permission_classes = [IsAuthenticated]
   queryset = MenuItem.objects.all()
   serializer_class = MenuItemSerializer