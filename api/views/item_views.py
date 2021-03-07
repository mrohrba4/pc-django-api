# rest_framework imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status

# Django imports
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user, authenticate, login, logout
from django.middleware.csrf import get_token

# model and serializer import
from ..models.item import Item
from ..serializers import ItemSerializer, UserSerializer

# Views
class Items(generics.ListCreateAPIView):
  permission_classes=(IsAuthenticated,)
  serializer_class = ItemSerializer

  # GET request
  def get(self, request):
    """'Index Items request'"""
    items = Item.objects.filter(owner=request.user.id)
    data = ItemSerializer(items, many=True).data
    return Response({ 'items': data })

  # POST request
  def post(self, request):
    """'Create Item request'"""
    # Add user to data object.
    request.data['item']['owner'] = request.user.id
    # Create Item
    item = ItemSerialier(data=request.data['item'])

    if item.is_valid():
      item.save()
      return Response({ 'item': item.data }, status=status.HTTP_201_CREATED)

    return Response(item.errors, status=status.HTTP_400_BAD_Request)

class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
  permission_classes=(IsAuthenticated,)
  # Show request
  def get(self, request, pk):
    """'Show Item request'"""

    # Locate the item to show
    item = get_object_or_404(Item, pk=pk)
    # Only show owned items
    if not request.user.id == entry.owner.id:
      raise PermissionDenied('Unauthorized, you do not own this item.')

    data = ItemSerializer(item).data
    return Response({ 'item': data })

  # DELETE request
  def delete(self, request, pk):
    """'Delete Item request'"""
    # Locate Item to delete
    entry = get_object_or_404(Item, pk=pk)

    # Check it requestor has permission.
    if not request.user.id == item.owner.id:
      raise PermissionDenied('Unauthorized, you do not own this item.')
    # only delete if user owns the item
    item.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
      """'Update Item request'"""
      if request.data['item'].get('owner', False):
        del request.data['item']['owner']

      entry = get_object_or_404(Item, pk=pk)

      if not request.user.id == item.owner.id:
        raise PermissionDenied('Unaquthorized, you do not own this item.')

      request.data['item']['owner'] = request.user.id

      data = ItemSerializer(item, data=request.data['item'])

      if data.is_valid():
        data.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

      return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
