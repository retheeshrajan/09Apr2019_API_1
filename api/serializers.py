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
        fields = ['name','description','price','image']

class ItemDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class ItemNameSerializer(serializers.ModelSerializer):
   class Meta:
        model = Item
        fields = ['name','image']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class OrderUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['status','total']


class CartCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

class CartUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['quantity',]

class CartListSerializer(serializers.ModelSerializer):
    item=ItemNameSerializer()
    class Meta:
        model = Cart
        fields = ['id','item','quantity','price']

class ItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


