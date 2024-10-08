from django.shortcuts import render,redirect
from Backend.models import prodb,martdb
from WebApp.models import contactdb,registerdb,cartdb,checkoutdb
from django.contrib import messages
import razorpay
# Create your views here.

def homepage(req):
    data=martdb.objects.all()
    return render(req,"Home.html",{'data':data})

def aboutpage(req):
    data=martdb.objects.all()
    return render(req,"About.html",{'data':data})

def contactpage(req):
    data = martdb.objects.all()
    return render(req,"contact.html",{'data':data})

def shoppage(req):
    data=prodb.objects.all()
    cat = martdb.objects.all()
    return render(req,"shop.html",{'data':data,'cat':cat})

def news_page(req):
    data=martdb.objects.all()
    return render(req,"News.html",{'data':data})

def save_contact(req):
    if req.method=="POST":
        na=req.POST.get("name")
        em=req.POST.get("email")
        ph=req.POST.get("phone")
        sub=req.POST.get("subject")
        mes=req.POST.get("message")
        ob=contactdb(Name=na,Email=em,Phone=ph,Subject=sub,Message=mes)
        ob.save()
        return redirect(contactpage)

def single_category(req,cat_name):
    cdata = martdb.objects.all()
    data=prodb.objects.filter(CatName=cat_name)
    cat=cat_name
    return render(req,"SingleCategory.html",{'data':data,'cdata':cdata,'cat':cat})

def single_product(req,pid):
    data=prodb.objects.get(id=pid)
    cat=martdb.objects.all()
    return render(req,"SingleProduct.html",{'data':data,'cat':cat})

def user_login(req):
    return render(req,"UserLogin.html")

def save_register(req):
    if req.method=="POST":
        una=req.POST.get("username")
        pas=req.POST.get("password")
        em=req.POST.get("email")
        cpas=req.POST.get("password2")
        ob=registerdb(Username=una,Password=pas,Email=em,Password2=cpas)
        if registerdb.objects.filter(Username=una).exists():
            messages.warning(req, "User already Exists!")
            return redirect(user_register)
        elif registerdb.objects.filter(Email=em).exists():
            messages.warning(req, "This Email already Exists!")
            return redirect(user_register)
        else:
            ob.save()
            messages.success(req, "Registered Successfully !")

        return redirect(user_login)

def loginbycheck(req):
    if req.method=="POST":
        un=req.POST.get("name")
        pas=req.POST.get("pass")
        em=req.POST.get("email")
        if registerdb.objects.filter(Username=un,Password=pas,Email=em).exists():
            req.session['username']=un
            req.session['password']=pas
            req.session['email']=em
            messages.success(req,"Login Success")
            return redirect(homepage)
        else:
            messages.warning(req,"Check Password and try again!!")

            return redirect(user_login)
    else:
        messages.error(req, "User not found!")

        return redirect(user_login)

def user_logout(request):
    del request.session['username']
    del request.session['password']
    messages.success(request, "Successfully Logout")

    return redirect(homepage)


def save_cart(req):
    if req.method=="POST":
        un=req.POST.get("username")
        pna=req.POST.get("proname")
        qn=req.POST.get("quantity")
        total=req.POST.get("total")
        ob=cartdb(Username=un,Productname=pna,Quantity=qn,Price=total)
        ob.save()
        messages.success(req,"Added to cart.")
        return redirect(homepage)

def cartpage(req):
    data = martdb.objects.all()
    cart=cartdb.objects.filter(Username=req.session['username'])
    tot_price=0
    shipping_charge=0
    grand_tot=0
    for i in cart:
        tot_price=tot_price+i.Price
        if tot_price<200:
            shipping_charge=50
        else:
            shipping_charge=20
        grand_tot=tot_price+shipping_charge


    return render(req,"cart.html",{"data":data,"cart":cart,"tot_price":tot_price,"shipping_charge":shipping_charge,"grand_tot":grand_tot})

def delete_cart(req,cid):
    data=cartdb.objects.filter(id=cid)
    data.delete()
    messages.success(req, "Removed")
    return redirect(cartpage)

def user_register(req):
    return render(req,"user_register.html")

def checkout_page(req):
    data=martdb.objects.all()
    cart = cartdb.objects.filter(Username=req.session['username'])
    tot_price = 0
    shipping_charge = 0
    grand_tot = 0
    for i in cart:
        tot_price = tot_price + i.Price
        if tot_price < 200:
            shipping_charge = 50
        else:
            shipping_charge = 20
        grand_tot = tot_price + shipping_charge

    return render(req, "CheckOut.html",{"data": data, "cart": cart, "tot_price": tot_price, "shipping_charge": shipping_charge,"grand_tot": grand_tot})

def payment(req):
    customer=checkoutdb.objects.order_by("-id").first()
    pay=customer.Total
    amount=int(pay*100)
    pay_str=str(amount)
    for i in pay_str:
        print(i)
    if req.method=="POST":
        order_currency="INR"
        client=razorpay.Client(auth=('rzp_test_UMVTetC6neXnFs','BDFnuQBfZAqcmYI1FpL1OC50'))
        payment=client.order.create({'amount':amount,'currency':order_currency,'payment_capture':'1'})
    return render(req,"Payment.html",{"customer":customer,"pay_str":pay_str})

def save_check(req):
    if req.method=="POST":
        na=req.POST.get("name")
        em=req.POST.get("email")
        add=req.POST.get("address")
        ph=req.POST.get("phone")
        des=req.POST.get("desc")
        tot=req.POST.get("total")
        ob=checkoutdb(Name=na,Email=em,Address=add,Phone=ph,Description=des,Total=tot)
        ob.save()
        return redirect(payment)
