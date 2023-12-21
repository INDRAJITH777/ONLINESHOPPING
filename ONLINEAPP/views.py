from django.shortcuts import render,redirect
from.models import *
from adminapp.models import *

# Create your views here.

def login(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['pass']

        if Customer.objects.filter(email=email,password=password).exists():
            data=Customer.objects.filter(email=email,password=password).values('cname','id').first()
            request.session['u_name']=data['cname']
            request.session['u_id']=data['id']
            request.session['u_email']=email
            request.session['u_password']=password
            return redirect('shopping')
    
        else:
            return redirect('signup')

    return render(request,'login.html')

def signup(request):
    if request.method=="POST":
        cname=request.POST['cname']
        email=request.POST['email']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']
        number=request.POST['number']

        if password==confirm_password:
            Customer.objects.create(
                cname=cname,
                email=email,
                password=password,
                number=number
            )
        else:
            return redirect('signup')
    return render(request,'signup.html')  

 


def online(request):
    return render(request,'online.html')
def shopping(request):
    categories = Category.objects.all()
    baskets=Shop.objects.all()
    context={
        "baskets":baskets,
        'categories':categories,
    }
    return render(request,'shopping.html', context)
def shop(request):
    basket=Shop.objects.all()
    context={
        "basket":basket
    }
    return render(request,'shop.html',context)


def cart(request):
    user_id= request.session['u_id']
    if request.method=="POST":
        price=request.POST['price']
        quantity=request.POST['quantity']
        product_id=request.POST['product_id']

        Cart.objects.create(
            price=price,
            quantity=quantity,
            product_id=Shop.objects.get(id=product_id),
            user_id=Customer.objects.get(id=user_id),
            total = int(price) * int(quantity),
        )
        return redirect('view_cart')
   
    
    return render(request,'single_product.html')
def view_cart(request):
    user_id= request.session['u_id']
    view_cart=Cart.objects.filter(user_id=user_id)
    total_amount=0
    for i in view_cart:
        total_amount+=i.total
    context={
        'view_cart':view_cart,
        'total_amount':total_amount
    }
    
    return render(request,'cart.html',context)
def about(request):
    return render(request,'about.html')



def checkout(request):
    return render(request,'checkout.html')
def single_product(request, product_id):
    items=Shop.objects.filter(id=product_id)
    other_products = Shop.objects.all().order_by('-id')[:4]

    context={
        "items":items,
        'other_products':other_products
    }
    return render(request,'single_product.html',context)

def filtered_products(request, category):
    products = Shop.objects.filter(type=category)
    context = {
        'products':products
    }
    return render(request, "filtered_products.html", context)

def delete_product3(request,product_id):
    Cart.objects.filter(id=product_id).delete()
    return redirect('view_cart')
