from django.contrib.auth.models import User
from rest_framework import serializers
from api.models import Item, Order, Cart

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'password','first_name','last_name','email']

    def create(self, validated_data):
        username = validated_data['username']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        email = validated_data['email']
        password = validated_data['password']
        new_user = User(username=username,first_name=first_name,last_name=last_name,email=email)
        new_user.set_password(password)
        new_user.save()
        return validated_data

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name','last_name','email']


class ItemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id','name','description','price','image']

class ItemDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class ItemNameSerializer(serializers.ModelSerializer):
   class Meta:
        model = Item
        fields = ['name','image']


class OrderSerializer(serializers.ModelSerializer):

    orderSum = serializers.SerializerMethodField()
    
    class Meta:
        model = Order
        fields = ['id','date','orderSum']

    def get_orderSum(self, obj):
        quantity = 0
        totalPrice = 0
        carts = Cart.objects.filter(order = obj)
        for i in carts:
            quantity = quantity + i.quantity  
            totalPrice = totalPrice + (i.quantity * i.price ) 
            orderSum = str(quantity)+' Item ' + str(totalPrice) +' KD'
        return orderSum

# class OrderSerializer(serializers.ModelSerializer):

#     orderQnty = serializers.IntegerField()
#     orderSum = serializers.DecimalField(max_digits=9, decimal_places=3)
    
#     class Meta:
#         model = Order
#         fields = ['id','date','orderQnty','orderSum']

class CheckOutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['status',]



class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

class CartListSerializer(serializers.ModelSerializer):
    item=ItemNameSerializer()
    class Meta:
        model = Cart
        fields = ['id','item','quantity','price']



