from django.shortcuts import render
from .serializers import ItemSerializer
from .models import Food
from rest_framework import generics, mixins

class ItemMixinView(
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView
):
    queryset = Food.objects.all()
    serializer_class = ItemSerializer
    lookup_field = 'pk'
    # Setting lookup_field value will be useful only if
    # lookup_field's value will be set to another value other than 'pk'
    # And it will be used only by Views that require lookup_field value
    # Example - RetrieveModelMixin requires it whereas ListModelMixin doesn't.

    def get(self, request, *args, **kwargs):
        if kwargs.get('pk'):
            return self.retrieve(request, *args, **kwargs)      # for Detail view
        return self.list(request, *args, **kwargs)      # for List view

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, partial=True, **kwargs)      # partial keyword must be set to true

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def perform_destroy(self, instance):
        super().perform_destroy(instance)
    # all perform_**** methods can be edited within this class to change functionality
    # of retrieve(), list(), create(), update() and destroy() methods.

    # generic API views have inherited generics.GenericAPIView and relevant mixin
    # Example - CreateAPIView == generics.GenericAPIView + mixins.CreateModelMixin
    # perform_create() is a method implemented within mixins.CreateModelMixin
    # So by editing that method in inherited class (in this case ItemMixinView)
    # we can change how a POST request is handled within post() function,
    # by editing perform_create() method.

# !!! As POST methods should not support url with 'pk' value and
# PUT, PATCH, DELETE should not support url without 'pk' value
# relevant conditional statements must be added to above methods
# to send responses with relevant error status codes
