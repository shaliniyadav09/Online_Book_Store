from django.shortcuts import render,redirect
from django.contrib import messages
from .models import  *
from adminapp.models import *
from userapp.models import *

def index(request):
     userid = request.session.get('userid')
     cart_count = 0
     if userid:
         user = UserInfo.objects.get(email=userid)
         cart = Cart.objects.filter(user=user)
         if not cart.exists():
             Cart.objects.create(user=user)
         cart = Cart.objects.get(user=user)
         cart_count = CartItem.objects.filter(cart=cart).count()
     context={
         'books' :Book.objects.all(),
         'userid':request.session.get('userid'),
         'cart_count' : cart_count
     }
     return render(request, 'index.html' ,context)
def about(request):
     context={
         'books' :Book.objects.all(),
         'userid':request.session.get('userid'),
     }
     return render(request, 'about.html' , context) 
def contact(request): # c-Create
    if request.method =="POST":
        name = request.POST.get('name') # first name is temp variable
        email = request.POST.get('email')
        contactno = request.POST.get('contactno')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        enq = Enquiry(name=name , email=email, contactno=contactno , subject=subject , message=message )#ORM
        enq.save()
        messages.success(request, 'Your message has been sent successfully')
        return redirect('contact')
    context={
         'userid':request.session.get('userid'),
     } 
    return render(request, 'contact.html',context)   
def login(request):
        if request.method=="POST":
         username=request.POST.get('username')
         password=request.POST.get('password')
         try:
            user =LoginInfo.objects.get(username=username,password=password , usertype="user")
            if user is not None:
                request.session['userid']=username
                messages.success(request , "Welcome User")
                return redirect('userdash')
         except LoginInfo.DoesNotExist:
            messages.error(request , 'Invalid username or password')
            return redirect('login')
        context={
         'userid':request.session.get('userid'),
     } 
        return render(request, 'login.html',context)   
def register(request):
      if request.method=="POST":
          name = request.POST.get('name')
          email = request.POST.get('email')
          contactno = request.POST.get('contactno')
          password = request.POST.get('password')
          cpassword = request.POST.get('cpassword')

          if password != cpassword:
              messages.error(request,"password and confirmpassword does not exist")
              
              return redirect('register')
          ch =LoginInfo.objects.filter(username=email)
          if ch:
              messages.error(request,"Email already exist")
              return redirect('register')
          log =LoginInfo(usertype="user" ,username=email,password=password)
          user = UserInfo(name=name,email=email,contactno=contactno ,login=log)
          
          log.save()
          user.save()
          messages.success(request,"Registration Successfull")
          return redirect('register')



      context={
         'userid':request.session.get('userid'),
     }
      return render(request, 'register.html',context)      

def dashboard(request):
    data={     #passing data from view to template
        'title':'dashboard'
    }
    return render(request,'dashboard.html' ,data)              
def  adminlogin(request):
    return render(request , 'adminlogin.html')

def adminlog(request):
    if request.method=="POST":
         username=request.POST.get('username')
         password=request.POST.get('password')
         try:
            admin =LoginInfo.objects.get(username=username,password=password , usertype="admin")
            if admin is not None:
                request.session['adminid']=username
                messages.success(request , "Welcom admin")
                return redirect('admindash')
         except LoginInfo.DoesNotExist:
            messages.error(request , 'Invalid username or password')
            return redirect('adminlogin')
    else:
        return redirect('adminlogin')
def book_details(request,id):
    context={
        'book':Book.objects.get(id=id),
        'userid':request.session.get('userid'),

    }    
    return render(request,"book_details.html" ,context)