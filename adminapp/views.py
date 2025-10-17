from django.shortcuts import render,redirect
from django.contrib import messages
from myapp.models import *
from userapp.models import *
from .models import *
from django.views.decorators.cache import cache_control
# Create your views here.
@cache_control(no_cache=True , no_store=True , must_revalidate=True)
def admindash(request): 
    if 'adminid' not in request.session:
        messages.error(request,"You are not logged in")
        return redirect('adminlogin')
    adminid=request.session.get('adminid')
    context={
        'adminid':adminid,
        'user_count': UserInfo.objects.all().count(),
        'book_count':Book.objects.all().count,
        'cat_count':Category.objects.all().count(),
        'order_count':Order.objects.all().count(),
        'enq_count':Enquiry.objects.all().count(),
    }       
    return render(request,'admindash.html',context)
def adminlogout(request):
    if 'adminid' in request.session:
        del request.session['adminid']
        messages.success(request,"you are logged out")
        return redirect('adminlogin')
    else:
        return redirect('adminlogin')
@cache_control(no_cache=True , no_store=True , must_revalidate=True)
def viewenqs(request): 
    if 'adminid' not in request.session:
        messages.error(request,"You are not logged in")
        return redirect('adminlogin')
    adminid=request.session.get('adminid')
    enqs=Enquiry.objects.all()
    context={
        'adminid':adminid,
         'enqs':enqs,
    }
    return render(request,'viewenqs.html',context)    
def delenqs(request ,id ): 
    if 'adminid' not in request.session:
        messages.error(request,"You are not logged in")
        return redirect('adminlogin')
    enq=Enquiry.objects.get(id=id)
    enq.delete()
    messages.success(request,"Enquiry deleted successfully")
    return redirect('viewenqs')

@cache_control(no_cache=True , no_store=True , must_revalidate=True)
def addcat(request): 
    if 'adminid' not in request.session:
        messages.error(request,"You are not logged in")
        return redirect('adminlogin')
    adminid=request.session.get('adminid')
    context={
        'adminid':adminid,
    }
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        cat = Category(name=name,description=description)   
        cat.save()
        messages.success(request,"Category added successfully")
        return redirect('addcat') # call addcat
    return render(request,'addcat.html',context)
@cache_control(no_cache=True , no_store=True , must_revalidate=True)
def viewcat(request): 
    if 'adminid' not in request.session:
        messages.error(request, "You are not logged in")
        return redirect('adminlogin')

    adminid = request.session.get('adminid')
    cats = Category.objects.all()

    context = {
        'adminid': adminid,
        'cats': cats
    }

    return render(request, 'viewcat.html', context) 

def delviewcat(request ,id ): 
    if 'adminid' not in request.session:
        messages.error(request,"You are not logged in")
        return redirect('adminlogin')
    cat=Category.objects.get(id=id)
    cat.delete()
    messages.success(request,"category deleted successfully")
    return redirect('viewcat')
    
     
@cache_control(no_cache=True , no_store=True , must_revalidate=True)
def addbook(request): 
    if 'adminid' not in request.session:
        messages.error(request,"You are not logged in")
        return redirect('adminlogin')
    adminid=request.session.get('adminid')
    cats=Category.objects.all()
    context={
        'adminid':adminid,
        'cats':cats
    }
    if request.method =="POST":
        title=request.POST.get('title')
        author=request.POST.get('author')
        category=request.POST.get('category')
        cat = Category.objects.get(id=category)
        description=request.POST.get('description')
        original_price=request.POST.get('original_price')
        price=request.POST.get('price')
        published_date=request.POST.get('published_date')
        language=request.POST.get('language')
        cover_image=request.FILES.get('cover_image')
        stock=request.POST.get('stock')
        b = Book(
            title=title ,
            author=author,
            category=cat,
            description=description,
            original_price=original_price,
            price=price,
            published_date=published_date,
            language=language,
            cover_image=cover_image,
            stock=stock
            )
        b.save()
        
        messages.success(request,"Book added successfully")
    return render(request,'addbook.html',context)
@cache_control(no_cache=True , no_store=True , must_revalidate=True)
def viewbook(request): 
    if 'adminid' not in request.session:
        messages.error(request,"You are not logged in")
        return redirect('adminlogin')
    adminid=request.session.get('adminid')
    book=Book.objects.all()
    context={
        'adminid':adminid,
         'book':book
    }
    return render(request,'viewbook.html',context)

def delbook(request ,id ): 
    if 'adminid' not in request.session:
        messages.error(request,"You are not logged in")
        return redirect('adminlogin')
    book=Book.objects.get(id=id)
    book.delete()
    messages.success(request,"Book deleted successfully")
    return redirect('viewbook')
@cache_control(no_cache=True , no_store=True , must_validate=True)
def editbook(request ,id): #update
    if 'adminid' not in request.session:
        messages.error(request,"You are not logged in")
        return redirect('adminlogin')
    adminid=request.session.get('adminid')
    book = Book.objects.get(id=id)
    cats=Category.objects.all()

    context={
        'adminid':adminid,
        'book':book,
        'cats':cats
    }
    if request.method =="POST":
        title=request.POST.get('title')
        author=request.POST.get('author')
        category=request.POST.get('category')
        cats = Category.objects.get(id=category)
        description=request.POST.get('description')
        original_price=request.POST.get('original_price')
        price=request.POST.get('price')
        published_date=request.POST.get('published_date')
        language=request.POST.get('language')
        cover_image=request.FILES.get('cover_image')
        stock=request.POST.get('stock')

        book.title=title
        book.author=author
        book.category=cats
        book.description=description
        book.original_price=original_price
        book.price=price
        if published_date:
              book.published_date=published_date
        book.language=language
        if cover_image:
              book.cover_image=cover_image
        book.stock=stock
        book.save()
        messages.success(request,f"{title} is updated successfully")
        return redirect('viewbook')      


    return render(request,'editbook.html',context)
