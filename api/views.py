from django.shortcuts import render
from rest_framework.generics import ListAPIView,RetrieveAPIView,RetrieveUpdateAPIView,DestroyAPIView,CreateAPIView
from .serializers import (ItemListSerializer, ItemDetailSerializer,UserCreateSerializer,CheckOutSerializer,OrderSerializer,
      UserUpdateSerializer,CartSerializer,CartListSerializer)
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from api.models import Item, Cart, Order
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils import timezone
import json
from django.core import serializers
from django.http import Http404
from rest_framework import status


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer

class UserUpdateView(APIView):

    def put(self, request):
        try:
            get_query = User.objects.get(pk = request.user.id)
            serializer = UserUpdateSerializer(get_query, data=request.data)
        except User.DoesNotExist:
            return  Response()  
        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self,request):
        try:
            get_query = User.objects.get(pk = request.user.id)
            serializer = UserUpdateSerializer(get_query, many=False,)  
        except User.DoesNotExist:
            return  Response()  
        return Response(serializer.data)

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


class CartListView(APIView):
    def get(self,request,id):
        get_query = Cart.objects.filter(order_id = id)
        serializer = CartListSerializer(get_query, many=True)
        return Response(serializer.data)  

class CartDeleteView(DestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'cart_id'

class OrderDetailView(APIView):
    def get(self,request):
        try:
            get_query = Order.objects.get(user_id = request.user.id,status = 0)
            serializer = OrderSerializer(get_query, many=False,)
        except Order.DoesNotExist:
            get_query = None   
            return Response(get_query)
        return Response(serializer.data)

class CheckOutView(RetrieveUpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = CheckOutSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'order_id'

class OrderHistoryView(APIView):
    def get(self,request):
        try:
            get_query = Order.objects.filter(user_id = request.user.id,status = 1)
            serializer = OrderSerializer(get_query, many=True,)
        except Order.DoesNotExist: 
            return Response()
        return Response(serializer.data)


class OrderControlAPIView(APIView):
    
    def post(self,request,item_id):

        try:
            items = Item.objects.get(id = item_id)
        except Item.DoesNotExist:
            items = None   
            return Response(items)
        try:
            orders = Order.objects.get(user= request.user, status=0)
            serializer = OrderSerializer(orders, many=False)
        except Order.DoesNotExist:
            orders=None

        if (orders):
            try:
                carts = Cart.objects.get(order = orders , item = items)
            except Cart.DoesNotExist:
                carts=None

            if(carts):
                self.UpdateCart(cart_id = carts.id,new_quantity = carts.quantity + 1)
            else:
               self.CreateCart(order = orders,item = items,item_price = items.price)

        else:
            orders = self.CreateOrder(item = items,item_price = items.price)
            serializer = OrderSerializer(orders, many=False)
        return Response(serializer.data)

    # Update the quantity of the cart item 
    def UpdateCart(self,cart_id,new_quantity):
        try:
            Cart.objects.filter(id = cart_id).update(quantity= new_quantity)
        except Cart.DoesNotExist:
            return None     

    # Create order and cart item 
    def CreateOrder(self,item,item_price):  
        orders= Order.objects.create(user=self.request.user,date = timezone.now(),status = 0,total = 0)
        self.CreateCart(order = orders,item = item,item_price = item_price)
        return orders

    def CreateCart(self,order,item,item_price):
        carts= Cart.objects.create(item= item,order=order,price = item_price ,quantity = 1)
        return carts





    # def OrderQnty(self,order):
    #     quantity = 0
    #     carts = Cart.objects.filter(order = order)
    #     for i in carts:
    #         quantity = quantity + i.quantity  
    #     return quantity

    # def OrderQnty(self,order):
    #     totalPrice = 0
    #     carts = Cart.objects.filter(order = obj)
    #     for i in carts:
    #         totalPrice = totalPrice + (i.quantity * i.price ) 
    #     return totalPrice;


class ContView():

    def retrieve_object(self,pk,obj):
        try:
            return obj.objects.get(pk = pk)
        except obj.DoesNotExist:
            return Http404  

    def retrieve(self, request,id):
        get_query = Order.objects,get(user_id = id)
        serializer = OrderSerializer(get_query)
        return Response(serializer.data)  

    # def update(self, request, pk):
        get_query = Order.objects.get(pk = pk)
        serializer = CheckOutSerializer(get_query, data=request.data)
        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, pk):
        get_query = Cart.objects.get(pk = pk)
        get_query.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



#
    



    






