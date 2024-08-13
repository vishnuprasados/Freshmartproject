from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Categories(models.Model):

    category=models.CharField(max_length=100)

    def __str__(self):
        return self.category




class Products(models.Model):

    product_name=models.CharField(max_length=100)

    category=models.ForeignKey(Categories,on_delete=models.CASCADE)

    description=models.CharField(max_length=100)

    quantity=models.CharField(max_length=100)

    price=models.PositiveIntegerField()

    image=models.ImageField(upload_to="media")


    def __str__(self):
        return self.product_name
    

class Cart(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE)

    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    netweight=models.CharField(max_length=100)




class PlaceOrder(models.Model):

    user= models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    post=models.CharField(max_length=100)
    pincode=models.PositiveIntegerField()
    mobile_no=models.PositiveIntegerField()
    email=models.EmailField()

    options=(
        ("order_placed","order_placed"),
        ("cancelled","cancelled"),
        ("dispatched","dispatched"),
        ("delivered","delivered")
    )
    status=models.CharField(max_length=100,choices=options,default="order_placed")












