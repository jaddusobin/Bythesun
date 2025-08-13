from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,"index.html")


def customerreg(request):
    if request.POST:
        username1=request.POST['username']
        email1=request.POST['email']
        phonenumber1=request.POST['phoneno']
        password1=request.POST['password']
        if'image' in request.FILES:
            image=request.FILES['image']
        else:
            # If image is not provided, assign a default image
            image='Image/client.jpg'
        address1=request.POST['address']
        if Customer.objects.filter(Email=email1).exists():
            messages.info(request,"Already Have Registered")
        else:
            customer=Login.objects.create_user(
            username=email1,password=password1,usertype='customer',viewPassword=password1)
            customer.save()
            register=Customer.objects.create(
            Username=username1,Email=email1,Phonenumber=phonenumber1,Password=password1,Image=image,Address=address1,customer=customer)
            register.save()
            messages.info(request,"Registered Successfully")
            return redirect("/login")
    return render(request,"customerreg.html")


def service_centerreg(request):
    if request.POST:
        servicecentername2=request.POST['username1']
        email2=request.POST['email1']
        phonenumber2=request.POST['phoneno1']
        password2=request.POST['password1']
        address2=request.POST['address1']
        if Service_center.objects.filter(Email1=email2).exists():
            messages.info(request,"Already Have Registered")
        else:
            servicecenter=Login.objects.create_user(
            username=email2,password=password2,usertype='service_center',viewPassword=password2)
            servicecenter.save()
            register1=Service_center.objects.create(
            Servicecentername1=servicecentername2,Email1=email2,Phonenumber1=phonenumber2,Password1=password2,Address1=address2,servicecenter=servicecenter)
            register1.save()
            messages.info(request,"Registered Successfully")
            return redirect("/login")
    return render(request,"servicecenterreg.html")


def login(request):
    if request.POST:
        Email2=request.POST['email2']
        Password2=request.POST['password2']
        user=authenticate(username=Email2,password=Password2)
        if user is not None:
            if user.usertype=="admin":
                messages.info(request,"Welcome To The Admin Page")
                return redirect("/adminhome")
            elif user.usertype=="customer":
                request.session['uid']=user.id
                messages.info(request,"Welcome To The Customer Page")
                return redirect("/customerhome")
            elif user.usertype=="service_center":
                request.session['uid']=user.id
                messages.info(request,"Welcome To The Service Center Page")
                return redirect("/servicecenterhome")
            else:
                messages.info(request,"Invalid Username Or Password")
                return redirect("/login")
        else:
            messages.info(request,"Invalid Username Or Password")
            return redirect("/login")
    return render(request,"login.html")


def adminhome(request):
    return render(request,"Admin/adminhome.html")


def customerhome(request):
    return render(request,"Customer/customerhome.html")


def service_centerhome(request):
    return render(request,"Servicecenter/servicecenterhome.html")


def viewcustomers(request):
    data=Customer.objects.all()
    return render(request,"Admin/viewcustomers.html",{"data":data})


def actioncustomers(request):
    id=request.GET['id']
    r=Customer.objects.filter(id=id).update(status='Approved')
    messages.info(request,"Approved Successfully")
    return redirect("/viewcustomers")


def rejectcustomers(request):
    id=request.GET.get('id')
    b=Customer.objects.filter(id=id).delete()
    e=Login.objects.filter(id=id).delete()
    messages.info(request,"Rejected successfully")
    return redirect("/viewcustomers")


def deletecustomers(request):
    id=request.GET['id']
    s=Customer.objects.filter(id=id)
    s.delete()
    messages.info(request,"Customer Deleted Successfully")
    return redirect("/viewcustomers")


def viewservice_center(request):
    data=Service_center.objects.all()
    return render(request,"Admin/viewservice_centers.html",{"data":data})


def actioncenters(request):
    id=request.GET['id']
    q=Service_center.objects.filter(id=id).update(status='Approved')
    messages.info(request,"Approved Successfully")
    return redirect("/viewcenters")


def rejectcenters(request):
    id=request.GET.get('id')
    o=Service_center.objects.filter(id=id).delete()
    w=Login.objects.filter(id=id).delete()
    messages.info(request,"Rejected successfully")
    return redirect("/viewcenters")


def deletecenters(request):
    id=request.GET['id']
    p=Service_center.objects.filter(id=id)
    p.delete()
    messages.info(request,"Service Center Deleted Successfully")
    return redirect("/viewcenters")


def addsolar_products(request):
    if request.POST:
        productname1=request.POST['productname']
        image3=request.FILES['image2']
        price1=request.POST['price']
        stock1=request.POST['stock']
        description1=request.POST['description'] 
        data=Solar_products.objects.create(Productname=productname1,Image1=image3,Price=price1,Stock=stock1,Description=description1)
        data.save()
        messages.info(request,"Added Successfully")
    return render(request,"Admin/addsolar_products.html")


def viewproducts(request):
    data=Solar_products.objects.all()
    return render(request,"Admin/viewproducts.html",{"data":data})


def editproducts(request):
    id=request.GET.get('id')
    edit=Solar_products.objects.filter(id=id)
    if request.POST:
        productname1=request.POST['productname']
        if 'image3' in request.FILES:
            image3=request.FILES.get('image2')
        else:
            image3=edit[0].Image1
        price1=request.POST['price']
        stock1=request.POST['stock']
        description1=request.POST['description']  
        product=Solar_products.objects.get(id=id)
        product.Productname=productname1
        product.Image1=image3
        product.Price=price1
        product.Stock=stock1
        product.Description=description1
        product.save()
        messages.info(request,"Updated Successfully")
        return redirect('/viewproducts')
    return render(request,'Admin/editproducts.html',{'edit':edit})


def viewsolar_products(request):
    data=Solar_products.objects.all()
    return render(request,"Customer/viewsolar_products.html",{"data":data})


def addfeedback(request):
    uid = request.session['uid']
    customer = Customer.objects.get(customer=uid)
    if request.POST:
        message1=request.POST['message']  
        data=Feedback.objects.create(Message=message1,customer=customer)
        data.save()
        messages.info(request,"Feedback Added Successfully")
    return render(request,"Customer/addfeedback.html")


def viewfeedback(request):
    data=Feedback.objects.all()
    return render(request,"Admin/viewfeedback.html",{"data":data})


def addreply(request): 
    id = request.GET.get("id")
    if request.method == 'POST':
        message2 = request.POST['message1']  
        feedback = Feedback.objects.filter(id=id).update(reply=message2, status="replied")
        messages.info(request,"Reply Added Successfully")
    return render(request, "Admin/addreply.html")


def viewproduct_detail(request):
    id=request.GET.get('id')
    data=Solar_products.objects.get(id=id)
    uid=request.session['uid']
    if request.POST:
        quantity = request.POST['qty']
        print(quantity)
        solarproducts = Solar_products.objects.get(id=id)
        customer = Customer.objects.get(customer=uid)
        price = int(solarproducts.Price)
        amt = int(price) * int(quantity)
        order, created = Order.objects.get_or_create(customer=customer, status='Pending', defaults={'amount': 0})
        order.amount = int(amt)
        order.save()
        cart_product = Cart.objects.filter( solarproducts=solarproducts, order=order).first()
        if cart_product:
            cart_product.qty += int(quantity)
            cart_product.amt += amt
            cart_product.save()
        else:
            # If the product is not already in the cart, create a new cart entry
            cart = Cart.objects.create(solarproducts=solarproducts, order=order, qty=quantity, amt=amt)
            cart.save()
            messages.info(request,"Item carted")
        return redirect('/viewcart')
    return render(request,'Customer/viewproduct_detail.html',{'data':data})


from django.http import Http404

def viewcart(request):
    try:
        uid = request.session['uid']
        customer = Customer.objects.get(customer=uid)
        order = Order.objects.filter(customer__customer_id=uid, status='Pending').first()
        
        if order is None:
            return render(request, 'Customer/viewcart.html', {'carts': [], 'oid': None})
        
        carts = Cart.objects.filter(order=order)
        return render(request, 'Customer/viewcart.html', {'carts': carts, 'oid': order.id})
    
    except KeyError:
       
        raise Http404("User not found")


def deletecart(request):
    id=request.GET.get('id')
    uid=request.session['uid']
    data=Cart.objects.get(id=id)
    oid = data.order.id
    cAmt = data.order.amount
    amt = data.amt
    order = Order.objects.get(id=oid)
    newAmt = int(cAmt) - int(amt)
    order.amount = newAmt
    order.save()
    data.delete()
    messages.info(request,"Item removed from cart")
    return redirect('/viewcart')


def addpayment(request):
    id = request.GET['id']
    order = Order.objects.get(id=id)
    if request.POST:
        order.status = "Paid"
        carts = Cart.objects.filter(order__id=id)
        for c in carts:
            pid = c.solarproducts.id
            qty = c.qty
            solarproducts = Solar_products.objects.get(id=pid)
            solarproducts.Stock = qty
            solarproducts.save()
            c.status = "Paid"
            c.save()
        order.save()
        messages.info(request,"Paid successfully")
        return redirect("/vieworder")
    amt = order.amount
    return render(request, "Customer/addpayment.html",{'amt':amt})


def vieworder(request):
    uid = request.session['uid']
    data = Order.objects.filter(customer__customer=uid, status='Paid')
    return render(request, 'Customer/vieworder.html', {"data":data})


def viewitems(request):
    uid = request.session['uid']
    id = request.GET['id']
    data = Cart.objects.filter(order__id=id)
    return render(request, "Customer/viewitems.html", {"data":data})


def vieworder_ad(request):
    data=Cart.objects.all()
    return render(request, "Admin/vieworder_ad.html", {"data":data})


def viewservice_centers(request):
    data=Service_center.objects.all()
    return render(request,"Customer/viewservice_centers.html",{"data":data})


def bookcenter(request):
    uid = request.session['uid']
    customer = Customer.objects.get(customer=uid)
    id = request.GET.get('id')
    servicecenter = Service_center.objects.get(id=id)
    products=Solar_products.objects.all()
    if request.POST:
        productname2=request.POST['products'] 
        message4=request.POST['message3'] 
        solarproducts = Solar_products.objects.get(id=productname2)
        data=Booking.objects.create(Productname1=productname2,Message2=message4,solarproducts=solarproducts,servicecenter=servicecenter,customer=customer)
        data.save()
        messages.info(request,"Booking successfully")
    return render(request,"Customer/addbooking.html",{'products':products})


def viewbooking(request):
    uid=request.session['uid']
    servicecenter=Service_center.objects.get(servicecenter=uid)
    data=Booking.objects.filter(servicecenter=servicecenter)
    return render(request,"ServiceCenter/viewbooking.html",{"data":data})

    
def actionbooking(request):
    id=request.GET['id']
    if request.POST:
        price2=request.POST['prices']
        m=Booking.objects.filter(id=id).update(Price1=price2,status='Approved')
        messages.info(request,"Price Add And Approved Successfully")
        return redirect("/viewbooking")
    return render(request,"ServiceCenter/addprice.html")


def rejectbooking(request):
    id=request.GET.get('id')
    l=Booking.objects.filter(id=id).delete()
    e=Login.objects.filter(id=id).delete()
    messages.info(request,"Rejected successfully")
    return redirect("/viewbooking")


def viewbooking_se(request):
    uid=request.session['uid']
    customer=Customer.objects.get(customer=uid)
    data=Booking.objects.filter(customer=customer)
    return render(request,"Customer/viewbooking_se.html",{"data":data})


def payment(request):
    uid = request.session['uid']
    customer = Customer.objects.get(customer=uid)
    id = request.GET.get('id')
    servicecenter = Service_center.objects.get(booking__id=id)
    if request.method == 'POST':
        payment = Booking.objects.filter(id=id).update(status="paid")
        messages.info(request,"Paid successfully")
    return render(request, "Customer/payment.html")


def viewpayment(request):
    uid=request.session['uid']
    servicecenter=Service_center.objects.get(servicecenter=uid)
    data=Booking.objects.filter(servicecenter=servicecenter)
    return render(request,"ServiceCenter/viewpayment.html",{"data":data})


def addrequest(request):
    uid = request.session['uid']
    customer = Customer.objects.get(customer=uid)
    if request.POST:
        unit1=request.POST['unit'] 
        message5=request.POST['message4']  
        data=Request.objects.create(Unit=unit1,Message2=message5,customer=customer)
        data.save()
        messages.info(request,"Send Request Added")
    return render(request,"Customer/sendrequest.html")


def viewrequest(request):
    data=Request.objects.all()
    return render(request,"Admin/viewrequest.html",{"data":data})


def actionrequest(request):
    id=request.GET['id']
    if request.POST:
        price3=request.POST['price1']
        y=Request.objects.filter(id=id).update(Price2=price3,status='Approved')
        messages.info(request,"Price Add And Approved Successfully")
        return redirect("/viewrequest")
    return render(request,"Admin/addprice.html")


def rejectrequest(request):
    id=request.GET.get('id')
    o=Request.objects.filter(id=id).delete()
    q=Login.objects.filter(id=id).delete()
    messages.info(request,"Rejected successfully")
    return redirect("/viewrequest")


def viewselling(request):
    data=Request.objects.all()
    return render(request,"Customer/viewselling.html",{"data":data})



