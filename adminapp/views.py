from django.shortcuts import render,redirect
from.models import *
from ONLINEAPP.models import *


# Create your views here.
def admin(request):
    return render(request,'admin.html')

def user_details(request):
    user=Customer.objects.all()
    context={
        'user':user
    }
    return render(request,'user_details.html',context)


def add_category(request):
    if request.method=='POST':
        type=request.POST['type']
       
        Category.objects.create(
         
            type=type,
         
        )

    return render(request,'add_category.html')



def add_product(request):
    categories=Category.objects.all()
    context={
        'categories':categories
    }
    if request.method=='POST':
        name=request.POST['name']
        type=request.POST['type']
        price=request.POST['price']
        image=request.FILES['image']

        Shop.objects.create(
            name=name,
            type=type,
            price=price,
            image=image
        )

    return render(request,'add_product.html',context)

def view_product(request):
    products=Shop.objects.all()
    context={
        'products':products
    }
    return render(request,'view_product.html',context)

def edit_product(request):
    view=Shop.objects.all()
    context={
        'view':view
    }
    return render(request,'edit_product.html',context)

def edit_changes(request,id):
    edit=Shop.objects.filter(id=id)
    context={
        'edit':edit
    }
    return render(request,'edit_changes.html',context)
def update(request,id):
    baskets=Shop.objects.filter(id=id)
    
    if request.method=='POST':
        name=request.POST['name']
        type=request.POST['type']
        price=request.POST['price']

        Shop.objects.filter(id=id).update(
            name=name,
            type=type,
            price=price
        )
        context={
            'baskets':baskets
        }
    return render(request,'edit_changes.html',context)

def delete_product(request):
    items=Shop.objects.all()
    context={
        'items':items
    }
    return render(request,'delete_product.html',context)

def delete_product2(request,id):
    Shop.objects.filter(id=id).delete()
    return redirect('delete_product')


def view_complaints(request):
    complaints=Contact.objects.all()
    context={
        'complaints':complaints
    }
    return render(request,'view_complaints.html',context)


def contact(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']

       
        Contact.objects.create(
         
            name=name,
            email=email,
            subject=subject,
            message=message
         
        )
    return render(request,'complaints.html')

def checkout(request):
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        country=request.POST['country']
        address=request.POST['address']
        city=request.POST['city']
        postcode=request.POST['postcode']
        phone=request.POST['phone']
        email=request.POST['email']

        Checkout.objects.create(
         
           fname=fname,
           lname=lname,
           country=country,
           address=address,
           city=city,
           postcode=postcode,
           phone=phone,
           email=email
         
        )
        return redirect('order')
    return render(request,'checkout.html')

def view_checkout(request):
    details=Checkout.objects.all()
    context={
        'details':details
    }
    return render(request,'view_checkout.html',context)

def order(request):
    return render(request,'orderplacing.html')