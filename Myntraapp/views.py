from django.contrib.auth import authenticate
from django.core.mail import send_mail
from Myntraproject.settings import EMAIL_HOST_USER
from django.shortcuts import render,redirect
from django.http import HttpResponse
import os
from .forms import *
from .models import*
from django.contrib.auth.models import User
import uuid
from django.contrib import messages
import datetime
from datetime import timedelta
# Create your views here.
def f(request):
    return render(request,'first.html')
def index(request):
    return render(request,'index.html')
def interpage(request):
    return render(request,'interpage.html')
def interpage2(request):
    return render(request,'interpage2.html')
def logshop(request):
    if request.method == 'POST':
            a = shoplogform(request.POST)
            if a.is_valid():
                    us = a.cleaned_data["shopname"] #myntra
                    ps = a.cleaned_data["password"]
                    # to make a variable global
                    request.session['shopname']=us
                    b = regshopmodels.objects.all()
                    for i in b:

                        if us == i.shopname and ps == i.password:
                            request.session['id']=i.id #1 id of shopuser
                            return redirect(shopprofile)
                            # if matched it wont go to else coz return can work one time execution stops there
                    else:
                        return HttpResponse("login failed")
    return render(request, 'shoplogin.html')
def shopprofile(request):
    shopname=request.session['shopname']
    return render(request,'profileshop.html',{'shopname':shopname})





def regshop(request):
        if request.method == 'POST':  # post should be uppercase(case sensitive )
            a = regshopform(
                request.POST)  # via data recieved through post method entered by the # user is passed to the regform(childclass) and is stored in a # nex is to check data is valid
            if a.is_valid():  # is_valid function used to check the validity of form fields
                us = a.cleaned_data["shopname"]
                sl = a.cleaned_data["shoploc"]
                id = a.cleaned_data["shopid"]
                em = a.cleaned_data["email"]
                mn = a.cleaned_data["mobnum"]
                ps = a.cleaned_data["password"]
                cp = a.cleaned_data["confirmpass"]  # cleaned_data = valid form fields are known as cleaned data
                if ps == cp:
                    b = regshopmodels(shopname=us,shoploc=sl,shopid=id,email=em, mobnum=mn,password=ps,confirmpass=cp
                                 )  # these are the fields of model(table ) cleaned data put into fileds
                    b.save()

                    return redirect(logshop)
            else:
                return HttpResponse("Registration failed ")

        return render(request,'shopregispg.html')
def reguser(request):
    return render(request,'cusregauth.html')
# def kurthacoll(request):
#     return render(request,'viewproductuser.html')
# def cart(request):
#     return render(request,'showcartother.html')
def uploadshop(request):
    if request.method=='POST':
        a=shopuploadform(request.POST,request.FILES)
        id=request.session['id'] #took this id from,now id has he id of the shop when created
        # snm=request.session['shopname']
        urid = request.session['userid']
        if a.is_valid():
            nm = a.cleaned_data['productname']
            pr = a.cleaned_data['productprice']
            ds = a.cleaned_data['productdescription']
            fl = a.cleaned_data['productfile']
            # userid = urid,
            b=shopuploadmodels(shopid=id,productname=nm,productprice=pr,productdescription=ds,productfile=fl)
            b.save()
            return redirect(imgdisplay)
        else:
            return HttpResponse('upload failed')
    return render(request,'uploadshop.html')
def imgdisplay(request):
    shpid=request.session['id']

    shpname=request.session['shopname']
    a=shopuploadmodels.objects.all() #image name , image file
    prdnm=[]
    prdprc=[]
    prdds=[]
    prdfl=[]
    id=[]
    shopid=[]
    shpnm=[]
    for i in a:
        sid=i.shopid
        shopid.append(sid)
        id1=i.id #listname and variable name should be diff
        nm=i.productname  # im has a path = "myapp/static/ganesha.png'
        pr=i.productprice
        ds=i.productdescription
        fl=i.productfile
        prdfl.append(str(fl).split('/')[-1])   #split is str fun thats why converted to str
        prdnm.append(nm)
        prdprc.append(pr)
        prdds.append(ds)
        id.append(id1)
    listcombining=zip(prdfl,prdnm,prdds,prdprc,id,shopid) #[(hello.png,hello)-->become one tupple]
    # why static  is coz image is in static file---> /static/image.png --->need to load this satitc
    #     check html page [(hello.png,hello)
    #  [(hello.png,hello)]-->tupple inside list we got i through zip()
    # so amount of data = i,j,k...  listcombining=zip(image,name)= i for image & j for name
    return render(request,"displayproduct.html",{'listcombining':listcombining,'shpid':shpid,'shpname':shpname})

def productdelete(request,id):
    a=shopuploadmodels.objects.get(id=id)
    a.delete()
    return redirect(imgdisplay)

def editproduct(request,id):
    a=shopuploadmodels.objects.get(id=id) #a=name,id,image,des,pri
    im=str(a.productfile).split('/')[-1]
    if request.method=='POST':
        if len(request.FILES):
            if len(a.productfile)>0:
                os.remove(a.productfile.path)
            a.productfile=request.FILES['productfile']
        a.productname=request.POST.get('productname')
        a.productprice=request.POST.get('productprice')
        a.productdesc= request.POST.get('productdesc')
        a.save()
        return redirect(imgdisplay)



    return render(request,"editproduct.html",{'a':a,'im':im})



def userregist(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email = request.POST.get('email')
        lastname = request.POST.get('lastname')
        firstname = request.POST.get('firstname')
        password= request.POST.get('password')
        #checking whether the username exist
        if User.objects.filter(username=username).first(): #username is in model=username
            #first():is for getting the first object from the filter function
            #message.success is a framework tat allows ou to sttore messages in one request and retrieve them in the request page
            messages.success(request,'username already taken')
            return redirect(userregist)
        if User.objects.filter(email=email).first():
            messages.success(request,'email already exist')
            return redirect(userregist) 
        user_obj=User(username=username,email=email,first_name=firstname,last_name=lastname)
        user_obj.set_password(password)
        #set_password: for securing password
        #then save
        #if a person is created a token should be generated
        user_obj.save()
        auth_token=str(uuid.uuid4()) # eg vd3er65..... this is stored as string
        profile_obj=profile.objects.create(user=user_obj,auth_token=auth_token) #storing token here
        profile_obj.save()
        #user defined function (send mail regis) which will be sep defined
        send_mail_registereduser(email,auth_token)#mail sending fun
        return render(request,'success.html')
        #to know whter mail is send or not
    return render(request,'cusregauth.html')
    # uuid module:stands for universally unique identifiers
        # four version available for token generaion we use uuid4()
# email,auth_token : attributes for getting email and auh_token
# send_mail('Subject here','Here is the message.','from@example.com',['to@example.com'],fail_silently=False,)
# f is a string literal which contains expressions inside curly brackets: the expressions are replaced by values (can pass values from out with f)
# its a list here mail id gets stored in email attribute
# inbuit function send_mail / send_mail_userregis is userdefined

def  send_mail_registereduser(email,auth_token):
    subject="your account has been verified"
    message=f'click the link to verify your acccount http://127.0.0.1:8000/Myntraapp/verify/{auth_token}'
    email_from=EMAIL_HOST_USER #from
    recipient=[email]
    send_mail(subject,message,email_from,recipient)
def verify(request,auth_token):
    profile_obj=profile.objects.filter(auth_token=auth_token).first()
    if profile_obj:
        if profile_obj.is_verified:
            messages.success(request,'your account is already verified')
            return redirect(loguser)
        profile_obj.is_verified=True
        profile_obj.save()
        messages.success(request, 'your account has been verified')
        return redirect(loguser)
    else:
        messages.success(request,'user not found')
        return redirect(loguser)


def showuserproduct(request):
    a = shopuploadmodels.objects.all()  # image name , image file

    prdnm = []
    prdprc = []
    prdds = []
    prdfl = []
    id = []
    for i in a:
        id1 = i.id  # listname and variable name should be diff
        nm = i.productname  # im has a path = "myapp/static/ganesha.png'
        pr = i.productprice
        ds = i.productdescription
        fl = i.productfile

        prdfl.append(str(fl).split('/')[-1])  # split is str fun thats why converted to str
        prdnm.append(nm)
        prdprc.append(pr)
        prdds.append(ds)
        id.append(id1)
    listcombining = zip(prdfl, prdnm, prdds, prdprc, id)  # [(hello.png,hello)-->become one tupple]
    # why static  is coz image is in static file---> /static/image.png --->need to load this satitc
    # check html page [(hello.png,hello)
    #  [(hello.png,hello)]-->tupple inside list we got i through zip()
    # so amount of data = i,j,k...  listcombining=zip(image,name)= i for image & j for name
    return render(request,'viewproductuser.html',{'listcombining': listcombining})
 # user_obj = User.objects.all()
        # for i in user_obj:
        #     request.session['userid'] = i.id
def loguser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        request.session['username']=username
        user_obj = User.objects.filter(username=username).first()
        request.session['id']=user_obj.id
        if user_obj is None:
            messages.success(request,'user not found')
            return redirect(loguser)
        profile_obj = profile.objects.filter(user=user_obj).first()
        if not profile_obj.is_verified:
            messages.success(request,'profile not verified check your mail')
            return redirect(loguser)
        user = authenticate(username=username,password=password)
        if user is None:
            messages.success(request,'wrong password or username')
            return redirect(loguser)

        return redirect(userprofile)

    return render(request,'custlogauth.html')

def userprofile(request):
    a=request.session['username']
    p=request.session['id']
    return render(request,'userprofile.html',{'a':a,'p':p})

def wishlistuser(request,id):
    o=request.session['id']

    a = shopuploadmodels.objects.get(id=id)
    if wishlist.objects.filter(productname=a.productname):
        return HttpResponse('already added')
    b = wishlist(uid=o,productname=a.productname, productprice=a.productprice, productdescription=a.productdescription,productfile=a.productfile)

    b.save()
    return HttpResponse('product added')
    # return render(request,'mywishlistuser.html')
def wishlistdisplay(request):
    uid=request.session['id']
    # unm=request.session['username']
    a=wishlist.objects.all()
    prdnm = []
    prdprc = []
    prdds = []
    prdfl = []
    id = []
    useri=[]
    for i in a:
        # if i.productname  not in prdnm:

         id1 = i.id  # listname and variable name should be diff
         nm = i.productname  # im has a path = "myapp/static/ganesha.png'
         pr = i.productprice
         ds = i.productdescription
         fl = i.productfile
         ui = i.uid
         prdfl.append(str(fl).split('/')[-1])  # split is str fun thats why converted to str
         prdnm.append(nm)
         prdprc.append(pr)
         prdds.append(ds)
         id.append(id1)
         useri.append(ui)
    # listcombining = zip(prdfl, prdnm, prdds, prdprc, id,useri)
    listcombining = zip(prdfl, prdnm, prdds, prdprc, id,useri)
    # print(prdnm,prdprc,prdds,prdfl,id,useri)
    # return render(request,'mywishlistuser.html',{'listcombining': listcombining,'uid':uid})
    return render(request,'mywishlistuser.html',{'listcombining': listcombining,'uid':uid})

def addcartuser(request,id):#7
    ucarid = request.session['id']
    a=shopuploadmodels.objects.get(id=id)
    if cart.objects.filter(productname=a.productname): #checking
        return HttpResponse("already in cart")
    b=cart(uc=ucarid,productname=a.productname,productprice=a.productprice,productdescription=a.productdescription,productfile=a.productfile)
    b.save()
    return HttpResponse('added to cart')

    # return render(request,'mycartuser.html')
def wishlisttocart(request,id):
    ucarid = request.session['id']
    a=wishlist.objects.get(id=id)
    if cart.objects.filter(productname=a.productname):
        return HttpResponse('Item already in cart')
    b=cart(uc=ucarid,productname=a.productname,productprice=a.productprice,productdescription=a.productdescription,productfile=a.productfile)
    b.save()
    return HttpResponse('added to cart')


def cartdisplay(request):
    cartdid= request.session['id']
    a=cart.objects.all()
    prdnm = []
    prdprc = []
    prdds = []
    prdfl = []
    id = []
    usercid=[]
    for i in a:
        id1 = i.id  # listname and variable name should be diff
        nm = i.productname  # im has a path = "myapp/static/ganesha.png'
        pr = i.productprice
        ds = i.productdescription
        fl = i.productfile
        uscid =i.uc
        prdfl.append(str(fl).split('/')[-1])  # split is str fun thats why converted to str
        prdnm.append(nm)
        prdprc.append(pr)
        prdds.append(ds)
        id.append(id1)
        usercid.append(uscid)
    listcombining = zip(prdfl, prdnm, prdds, prdprc, id,usercid)
    return render(request,'mycartuser.html',{'listcombining': listcombining,'cartdid':cartdid})

def removefromcart(request,id):
    a=cart.objects.get(id=id)
    a.delete()
    return redirect(cartdisplay)


def rmvproductwishlist(request,id):
    a=wishlist.objects.get(id=id)
    a.delete()
    return redirect(wishlistdisplay)

def buyproduct(request,id):
    a=cart.objects.get(id=id)
    fl = a.productfile
    x = str(fl).split('/')[-1]
    if request.method=='POST':
        nm = request.POST.get('productname')
        pr = request.POST.get('productprice')
        des = request.POST.get('productdescription')
        quan = request.POST.get('quantity')
        b=buy(productname=nm,productprice=pr,productdescription=des,quantity=quan)
        b.save()
        total=int(pr)*int(quan)
        return render(request,'finalbill.html',{'tt':total,'nm':nm,'pr':pr,'quan':quan,'x':x})
    return render(request,'buypdt.html',{'a':a,'fl':x})

def cardpay(request):
        if request.method == 'POST':
            a =customercardpay(request.POST)
            if a.is_valid():
                nm = a.cleaned_data['cardname']
                pr = a.cleaned_data['cardnumber']
                ds = a.cleaned_data['cardexpiry']
                fl = a.cleaned_data['securitycode']
                b = customercard(cardname=nm, cardnumber=pr, cardexpiry=ds, securitycode=fl)
                c = datetime.date.today()
                v = c + timedelta(15)
                return render(request, 'orderstatus.html', {'v': v})
            else:
                return HttpResponse('something wrong happened')
        return render(request, 'cardpayment.html')


def showotherproducts(request):
    a = shopuploadmodels.objects.all()  # image name , image file
    # shpid=request.session['id']
    # request.session ['id']=
    prdnm = []
    prdprc = []
    prdds = []
    prdfl = []
    # id = []

    for i in a:
        # sid = i.shopid
        # shopid.append(sid)
        id1 = i.id  # listname and variable name should be diff
        nm = i.productname  # im has a path = "myapp/static/ganesha.png'
        pr = i.productprice
        ds = i.productdescription
        fl = i.productfile

        prdfl.append(str(fl).split('/')[-1])  # split is str fun thats why converted to str
        prdnm.append(nm)
        prdprc.append(pr)
        prdds.append(ds)

        # id.append(id1)
    listcombining = zip(prdfl, prdnm, prdds, prdprc)
    return render(request,'viewothershop.html',{'listcombining':listcombining})

# def shopnotif(request):
#     a=shopnotification.objects.all()
#     return redirect(shopnotdisplay)
def shopnotif(request):
    a = shopnotification.objects.all()  # image name , image file
    shopnottime=[]
    cont = []
    for i in a:
        # listname and variable name should be diff
        tm=i.shopnottime
        ct = i.content  # im has a path = "myapp/static/ganesha.png'
        cont.append(ct)
        shopnottime.append(tm)
    s=zip(shopnottime,cont)
    print(shopnottime)

    return render(request, 'shopnoti.html',{'s':s})
def usernotif(request):
    a = usernotification.objects.all()  # image name , image file
    usernottime = []
    cont = []
    for i in a:
        # listname and variable name should be diff
        ct = i.content  # im has a path = "myapp/static/ganesha.png'
        cont.append(ct)
        ut=i.usernottime
        usernottime.append(ut)
    s=zip(usernottime,cont)

    return render(request, 'usernoti.html',{'s':s})
# def customerlocation(request):
#     if request.method == 'POST':
#         a = customerlocationform(request.POST)
#         if a.is_valid():
#             nm = a.cleaned_data['name']
#             pr = a.cleaned_data['number']
#             ds = a.cleaned_data['address']
#             fl = a.cleaned_data['pincode ']
#             n = a.cleaned_data['locality']
#             p = a.cleaned_data['city']
#             f = a.cleaned_data['state']
#             b = customerlocationmodel(name=nm, number =pr,address=ds, pincode=fl,locality=n,city=p,state=f )
#             b.save()
#             c = datetime.date.today()
#             v = c + timedelta(15)
#             return render(request,'orderstatus.html', {'v': v})
#         else:
#             return HttpResponse('something wrong happened')
#     return render(request, 'customerlocation.html')
    # name
    #    number
    #    address
    #    pincode
    #    locality
    #    city
    #    state
# import datetime
# from datetime import timedelta
# a=datetime.date.today()
# b=a+timedelta(15)
# print(b)

        # user_obj.set_password(password)
    # auth_token = str(uuid.uuid4())  # eg vd3er65..... this is stored as string
    # profile_obj = profile.objects.create(user=user_obj, auth_token=auth_token)  # storing token here
    # profile_obj.save()
    # user defined function (send mail regis) which will be sep defined
    # send_mail_registereduser(email, auth_token)  # mail sending fun
#
# def orderstatus(request):
#     return render(request,'orderstatus.html')
def contactus(request):
    return render(request,'contact.html')
def aboutus(request):
    return render(request,'aboutus.html')
