from django.http import  JsonResponse
from django.http import HttpResponse
from django.shortcuts import redirect,render
from django.contrib import messages
from .models import Cart,Order,OrderItem,Product,Profile
from django.contrib.auth.models import User
import random
import razorpay
def index(request):
    cart = Cart.objects.filter(user=request.user)
    for item in cart:
        if item.product_qty > item.product.quantity:
            Cart.objects.delete(id=item.id)
    
    cartitems = Cart.objects.filter(user=request.user)
    total_cost = 0
    for item in cartitems:
        total_cost=total_cost + item.product_qty * item.product.selling_price
    
    userprofile = Profile.objects.filter(user=request.user).first()


    context = {'cartitems':cartitems,'total_cost':total_cost,'userprofile':userprofile} 
    return render(request,'shop/checkout.html',context)

def placeorder(request):
    if request.method=='POST':

        currentuser = User.objects.filter(id=request.user.id).first()
        
        if not currentuser.first_name:
            currentuser.first_name = request.POST.get('name')
            currentuser.last_name = request.POST.get('lname')
            currentuser.save()

        if not Profile.objects.filter(user=request.user):
            userprofile = Profile()
            userprofile.user=request.user
            userprofile.phone=request.POST.get('phone')
            userprofile.address=request.POST.get('address')
            userprofile.city=request.POST.get('city')
            userprofile.state=request.POST.get('state')
            userprofile.country=request.POST.get('country')
            userprofile.pincode=request.POST.get('pincode')
            userprofile.save()

        neworder= Order()
        neworder.user=request.user
        neworder.name=request.POST.get('name')
        neworder.name=request.POST.get('lname')
        neworder.email=request.POST.get('email')
        neworder.phone=request.POST.get('phone')
        neworder.address=request.POST.get('address')
        neworder.city=request.POST.get('city')
        neworder.state=request.POST.get('state')
        neworder.country=request.POST.get('country')
        neworder.pincode=request.POST.get('pincode')
        neworder.payment_mode=request.POST.get('payment_mode')
        neworder.payment_id=request.POST.get('payment_id')

        cart=Cart.objects.filter(user=request.user)
        cart_total_cost=0
        for item in cart:
            cart_total_cost=cart_total_cost + item.product_qty * item.product.selling_price
        
        neworder.total_cost = cart_total_cost
        trackno=''+str(random.randint(1111111,9999999))
        while Order.objects.filter(tracking_no=trackno) is None:
            trackno=''+str(random.randint(1111111,9999999))

        neworder.tracking_no = trackno
        neworder.save()

        neworderitems = Cart.objects.filter(user=request.user)
        for item in neworderitems:
            OrderItem.objects.create(
                order=neworder,
                product=item.product,
                price=item.product.selling_price,
                quantity=item.product_qty
            )
            #to decrease the product quantity from available stock
            orderproduct = Product.objects.filter(id=item.product_id).first()
            orderproduct.quantity = orderproduct.quantity - item.product_qty
            orderproduct.save()

        #to clear user cart
        Cart.objects.filter(user=request.user).delete()
        
        messages.success(request,"your order has been placed successfully")
        
        payMode = request.POST.get('payment_mode')
        if(payMode == "Paid by Razorpay"):
            return JsonResponse({'status':"Your order has been placed successfully"})
        else:
            messages.success(request,"your order has been placed successfully")
    return redirect('/')

def razorpaycheck(request):
    cartitems = Cart.objects.filter(user=request.user)
    total_cost = 0
    for item in cartitems:
        total_cost=total_cost + item.product_qty * item.product.selling_price
    return JsonResponse({
        'total_cost': total_cost
    })

def myorders(request):
    return HttpResponse("My orders page")







