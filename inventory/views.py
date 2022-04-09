from typing import AnyStr
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from .models import ItemMain, ItemsCat, UserCart, Contact
import json
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.


def home(request):
    context = {}
    return render(request, "homepage.html", context)


def items_display(request):
    itemsearch = []
    l = list(ItemMain.objects.all())
    if request.method == 'POST':
        search_keyword = request.POST.get('search_keyword')
        if search_keyword != "" and search_keyword != None:
            item_search_part1 = list(ItemMain.objects.filter(
                itemname__icontains=search_keyword))
            item_search_part2 = list(ItemMain.objects.filter(
                composition__icontains=search_keyword))
            item_search_part3 = list(ItemMain.objects.filter(
                itemid__icontains=search_keyword))
            itemsearch = item_search_part1 + item_search_part2 + item_search_part3
            if itemsearch == []:
                messages.info(request, 'No Results Found')
        else:
            itemsearch = list(ItemMain.objects.all())
        cat = request.POST.getlist('cat', [])
        print(cat)
        min_price = request.POST.get('min_price')
        max_price = request.POST.get('max_price')
        if min_price == '':
            min_price = 0
        else:
            min_price = int(min_price)
        if max_price == '':
            max_price = 10000000
        else:
            max_price = int(max_price)
        items = []
        if len(cat) > 0:
            if (len(cat)):
                items = ItemMain.objects.filter(
                    type__in=ItemsCat.objects.filter(catName__in=cat))
        else:
            items = ItemMain.objects.all()
        print(list(items))
        print(itemsearch)
        items = list(set(items).intersection(set(itemsearch)))
        l = []
        for i in items:
            ll = []
            ll.append(i.itemid)
            ll.append(i.itemname)
            ll.append(i.expirydate)
            ll.append(i.discount)
            ll.append(i.price)
            price = i.price
            offer = i.discount
            newPrice = price - (price * offer)/100
            ll.append(newPrice)
            if newPrice >= min_price and newPrice <= max_price:
                ll.append("Valid")
            else:
                ll.append("Invalid")
            ll.append(i.slug)
            l.append(ll)
        print(l)
    context = {
        "items": l
    }
    return render(request, "inventory/inventory view.html", context)

# @login_required(login_url='login')


def item_upload(request):
    context = {}
    if request.method == 'POST':
        itemname = request.POST.get('itemname')
        discount = int(request.POST.get('discount'))
        price = int(request.POST.get('price'))
        type = request.POST.get('category', "medicine")
        quantity = int(request.POST.get('quantity'))
        composition = request.POST.get('description')
        manufacturingdate = request.POST.get('manufacturingdate')
        expirydate = request.POST.get('expirydate')
        itemsearch = list(ItemMain.objects.filter(
            itemname__icontains=itemname, price=price, discount=discount, expirydate=expirydate))
        if itemsearch == []:
            itemmain = ItemMain.objects.create(
                itemname=itemname,
                discount=discount,
                price=price,
                type=ItemsCat.objects.filter(catName=type)[0],
                quantity=quantity,
                composition=composition,
                manufacturingdate=manufacturingdate,
                expirydate=expirydate
            )
            itemmain.save()
        else:
            itemsearch[0].update_quantity(quantity)
            itemsearch[0].save()

    return render(request, 'inventory/inventoryadd.html', context)

# @login_required(login_url='login')


def cart(request):
    context = {}
    if request.method == "GET":
        user = request.user
        items = UserCart.objects.filter(
            user=User.objects.filter(username=user)[0]
        )
        l = []
        for i in items:
            ll = []
            item = ItemMain.objects.filter(itemid=i.itemid)[0]
            ll.append(i.title)
            ll.append(item.composition)
            price = item.price
            discount = item.discount
            newPrice = price - (price * discount)//100
            ll.append(newPrice)
            ll.append(i.total)
            ll.append(newPrice*i.quantity)
            l.append(ll)
        context['items'] = l
    return render(request, 'inventory/cart.html', context)

# @login_required(login_url='login')
# def clear_cart(request):
#     context = {}
#     if request.method == "GET":
#         user = request.user
#         items = UserCart.objects.filter(
#             user = User.objects.filter(username = user)[0]
#             )
#         l = []
#         for i in items:
#             ll = []
#             item =ItemMain.objects.filter(title = i.title)[0]
#             ll.append(ItemsImages.objects.filter(title=item)[0].image)
#             ll.append(i.title)
#             ll.append(item.description)
#             price = item.price
#             offer = item.offers
#             newPrice = price - (price * offer)//100
#             ll.append(newPrice)
#             ll.append(i.total)
#             l.append(ll)
#             i.delete()
#         context['items'] = l
#         return redirect('cart')


def contact(request):
    if request.method == "POST":
        username = request.POST.get("username")
        phone = request.POST.get("phone")
        problem = request.POST.get("problem")
        contact = Contact.objects.create(
            username=username, phone=phone, problem=problem)
        contact.save()
    return render(request, "contactus.html", {})
