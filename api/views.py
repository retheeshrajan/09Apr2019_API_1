from django.shortcuts import render
from rest_framework.generics import ListAPIView,RetrieveAPIView,RetrieveUpdateAPIView,DestroyAPIView,CreateAPIView
from .serializers import (ItemListSerializer, ItemDetailSerializer,UserCreateSerializer,OrderDetailSerializer,OrderUpdateSerializer,OrderCreateSerializer,
	CartCreateSerializer,CartListSerializer,UserUpdateSerializer)
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from api.models import Item, Cart, Order
from django.contrib.auth.models import User

class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer

class UserUpdateView(RetrieveUpdateAPIView):
	queryset = User.objects.all()
	serializer_class = UserUpdateSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'user_id'

class ItemListView(ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemListSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['name','description','price','category']

class ItemDetailView(RetrieveAPIView):
	queryset = Item.objects.all()
	serializer_class = ItemDetailSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'item_id'

class OrderCreateAPIView(CreateAPIView):
    serializer_class = OrderCreateSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class OrderUpdateView(RetrieveUpdateAPIView):
	queryset = Order.objects.all()
	serializer_class = OrderUpdateSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'order_id'

class OrderDetailView(RetrieveAPIView):
	queryset = Order.objects.filter(status = 0)
	serializer_class = OrderDetailSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'user_id'

class CartListView(ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartListSerializer
    filter_backends = [SearchFilter]
    search_fields = ['order',]

class CartCreateAPIView(CreateAPIView):
    serializer_class = CartCreateSerializer

