from django.shortcuts import render
from rest_framework.views import APIView
from ecommapp.serializers import ProductSerializer,UserSerializer,CartSerializer,CategorySerializer,PlaceOrderSerializer
from ecommapp.models import Products,Categories,Cart
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import authentication,permissions
from rest_framework import viewsets
from rest_framework.decorators import action

# Create your views here.








class UserView(viewsets.ViewSet):

  def create(self,request,*args,**kwargs):
     serializer=UserSerializer(data=request.data)

     if serializer.is_valid():
         serializer.save()

         return Response(data=serializer.data)
     
     else:
        return Response({'msg':"invalid"})
class ProductView(viewsets.ModelViewSet):

    serializer_class=ProductSerializer
    queryset=Products.objects.all()

    permission_classes=[permissions.IsAuthenticated]
    authentication_classes=[authentication.TokenAuthentication]

    @action(methods=['GET'],detail=False)
    def category_list(self,request):
        category=Categories.objects.values_list('category',flat=True)
        return Response(data=category)
    

    @action(methods=["POST"],detail=True)

    def addto_cart(self,request,*args,**kwargs):
        id = kwargs.get("pk")
        item= Products.objects.get(id=id)
        user = request.user

        user.cart_set.create(product=item)
        return Response(data="item added to cart")
    

    # def listby_category(self,request,*args, **kwargs):

    

class CartsView(viewsets.ModelViewSet):

    serializer_class=CartSerializer
    queryset = Cart.objects.all()

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

    @action(methods=["POST"],detail=True)

    def place_order(self,request,*args, **kwargs):
        serializer=PlaceOrderSerializer(data=request.data)
        pdt_object=Products.objects.get(id=kwargs.get('pk'))
        user=request.user
        if serializer.is_valid():
            serializer.save(product=pdt_object,user=user)
            return Response(data=serializer.data)
        return Response(data=serializer.errors)
    

    

class Listbycategory(viewsets.ModelViewSet):

    serializer_class=CategorySerializer
    queryset = Categories.objects.all()

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    # def get_queryset(self):
    #     return Products.objects.filter(Categories=self.request.user)
    @action(methods=['get'],detail=True)
    def listby_category(self,request,*args, **kwargs):
        id=kwargs.get('pk')
        cat=Categories.objects.get(category=id)
        products=Products.objects.filter(category=cat)
        serializer=ProductSerializer(products,many=True)
        return Response(data=serializer.data)


class CartDelete(viewsets.ModelViewSet):

    serializer_class=CartSerializer

    queryset = Cart.objects.all()
    authentication_classes=[authentication.TokenAuthentication]

    @action(methods=["delete"],detail=True)
    
    def cart_delete(self,request,*args, **kwargs):
        cart_item= self.get_object()

        if cart_item.user != request.user:

            return Response("no permissin to delete")

        cart_item.delete()

        return Response("item deleted") 
        









