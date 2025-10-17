from django.urls import path
from . import views
urlpatterns =[
    path('userdash/' , views.userdash,name="userdash"),
    path('userlogout/' , views.userlogout,name="userlogout"),
    path('userprofile/' , views.userprofile,name="userprofile"),
    path('editprofile/' , views.editprofile,name="editprofile"),
    path('viewcart/' , views.viewcart,name="viewcart"),
    path('userorders/' , views.userorders,name="userorders"),
    path('removeitems/<id>' , views.removeitems,name="removeitems"),
    path('addtocart/<id>' , views.addtocart,name="addtocart"),
    path('checkout/' , views.checkout,name="checkout"),
    path('changepassword/' , views.changepassword, name="changepassword"),
    path('payment-success/' , views.payment_success,name="payment_success"),
]