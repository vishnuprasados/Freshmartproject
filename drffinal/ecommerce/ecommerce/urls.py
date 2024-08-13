"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from ecommapp import views
from rest_framework.authtoken.views import ObtainAuthToken
from django.conf import settings
from django.conf.urls.static import static

router=DefaultRouter()

router.register("products",views.ProductView,basename="productlist")
router.register("user",views.UserView,basename="user")
router.register("carts",views.CartsView,basename="carts")
router.register("cat/list",views.Listbycategory,basename="category")
router.register("cart/delete",views.CartDelete,basename="cartdelete")

 




urlpatterns = [
    path('admin/', admin.site.urls),
    path('token/',ObtainAuthToken.as_view()),
]+router.urls+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
