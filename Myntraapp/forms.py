from django import forms


class regshopform(forms.Form):
    shopname = forms.CharField(max_length=30)
    shoploc = forms.CharField(max_length=30)
    shopid = forms.IntegerField()
    email = forms.EmailField()
    mobnum = forms.IntegerField()
    password = forms.CharField(max_length=30)
    confirmpass = forms.CharField(max_length=30)
class shoplogform(forms.Form):
    shopname = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30)
class shopuploadform(forms.Form):
    productname =forms.CharField(max_length=30)
    productprice=forms.IntegerField()
    productdescription=forms.CharField(max_length=150)
    productfile=forms.ImageField()
    # userid=forms.IntegerField()

class imgdisplay(forms.Form):
        productname = forms.CharField(max_length=30)
        productprice = forms.IntegerField()
        productdescription = forms.CharField(max_length=150)
        productfile = forms.ImageField()

class customercardpay(forms.Form):
    cardname= forms.CharField(max_length=30)
    cardnumber= forms.CharField(max_length=30)
    cardexpiry= forms.CharField(max_length=30)
    securitycode=forms.CharField(max_length=30)

# class customerlocationform(forms.Form):
#     name= forms.CharField(max_length=10)
#     number = forms.IntegerField()
#     address= forms.CharField(max_length=30)
#     pincode = forms.IntegerField()
#     locality= forms.CharField(max_length=30)
#     city = forms.CharField(max_length=10)
#     state = forms.CharField(max_length=10)

