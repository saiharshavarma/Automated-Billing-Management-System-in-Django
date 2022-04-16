from statistics import quantiles
from typing import AnyStr
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from .models import CustomerDetails, Medicine_Logs
from inventory.models import UserCart, ItemMain
from inventory.views import empty_cart
import json
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='login')
def customer_details(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            first_name = request.POST['first_name']
            middle_name = request.POST['middle_name']
            last_name = request.POST['last_name']
            state = request.POST['state']
            street = request.POST['street']
            city = request.POST['city']
            phone = request.POST['phone']
            email = request.POST['email']
            billing = CustomerDetails.objects.create(first_name=first_name, middle_name=middle_name, last_name=last_name,
                                                     state=state, street=street, city=city, phone=float(phone), email=email)
            billing.save()
            return redirect('bill')
        else:
            return redirect('login')
    else:
        return render(request, 'checkout/customer details.html', {})


@login_required(login_url='login')
def generate_bill(request):
    context = {}
    customer = list(CustomerDetails.objects.all())[-1]
    context['customer'] = customer
    total_amount = 0
    if request.method == "GET":
        user = request.user
        items = UserCart.objects.filter(
            user=User.objects.filter(username=user)[0]
        )
        l = {}
        for i in items:
            ll = []
            item = ItemMain.objects.filter(slug=i.itemid)[0]
            ll.append(item.itemid)
            ll.append(item.itemname)
            price = item.price
            discount = item.discount
            newPrice = price - (price * discount)/100
            ll.append(newPrice)
            if tuple(ll) in l.keys():
                l[tuple(ll)] += 1
            else:
                l[tuple(ll)] = 1
            total_amount += newPrice
        for item, quantity in l.items():
            itemtemp = ItemMain.objects.filter(slug=item[0])[0]
            log = Medicine_Logs.objects.create(
                user=user, customer=customer, itemid=itemtemp, quantity=quantity, price=item[2]*quantity)
            log.save()
        empty_cart(request)
        print(l)
        context['items'] = l
        context['total'] = total_amount
    return render(request, "checkout/bill.html", context)
