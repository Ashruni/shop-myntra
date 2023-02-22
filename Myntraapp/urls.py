from django.urls import path
from.views import *
urlpatterns=[
   path('f/',f),
   path('index/',index),
   path('inpage/',interpage),
    path('inpage2/',interpage2),
    path('logshop/',logshop),
    path('loguser/',loguser),
    path('regshop/',regshop),
    path('reguser/',userregist),
    #path('kurthas/',kurthacoll),
    #path('showcart/',cart),
    path('productupload/',uploadshop),
    path('shopprofile/',shopprofile),
    path('imagedisplay/',imgdisplay),
    path('delete/<int:id>/',productdelete),
    path('edit/<int:id>/',editproduct),
    path('verify/<auth_token>',verify),#string
    path('userprofile/',userprofile),
    path('showuser/',showuserproduct),
    path('wishlistuser/<int:id>/',wishlistuser),
    path('wishlistproduct/',wishlistdisplay),
    path('addcartuser/<int:id>/',addcartuser),
    path('addcartproduct/',cartdisplay),
    path('removefromwishlist/<int:id>/',rmvproductwishlist),
    path('cartbuy/<int:id>/',buyproduct),
    path('removefromcart/<int:id>/',removefromcart),
    path('wishlisttocart/<int:id>/',wishlisttocart),
    path('cardpayment/',cardpay),
    path('showotherproducts/',showotherproducts),
    path('contactus/',contactus),
    path('aboutus/',aboutus),
    path('shopnot/',shopnotif),
    path('usernot/',usernotif),

     #path('customerlocation/',customerlocation),

    #path('status/',orderstatus),



]