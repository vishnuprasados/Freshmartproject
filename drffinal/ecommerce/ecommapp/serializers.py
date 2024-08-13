

from rest_framework import serializers

from ecommapp.models import Products,Cart,Categories,PlaceOrder

from django.contrib.auth.models import User





class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products

        

        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
    product=ProductSerializer(read_only=True)
    class Meta:
        model= Categories

        fields="__all__"


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["first_name","last_name","email","username","password"]
    
    def create(self,validated_data):

        return User.objects.create_user(**validated_data)
    

class CartSerializer(serializers.ModelSerializer):
    product=ProductSerializer(read_only=True)
    user = serializers.CharField(read_only=True)
    date = serializers.CharField(read_only=True)

    class Meta:
        model=Cart

        fields="__all__"

class PlaceOrderSerializer(serializers.ModelSerializer):
    product=ProductSerializer(read_only=True)
    user = serializers.CharField(read_only=True)
    date = serializers.CharField(read_only=True)


    class Meta:
        model=PlaceOrder
        fields="__all__"