from typing import AnyStr
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from .models import ItemMain, ItemsCat, UserCart
import json
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    context = {}
    return render(request, "homepage.html", context)

# def items_display(request):    
#     cat = request.GET.getlist('cat', [])
#     offerss = request.GET.getlist('offer', [])
#     items = []
#     offerss = list(map(int, offerss))
#     if len(offerss) > 0:
#         min_off = min(offerss)
#     if len(cat) > 0 or len(offerss) > 0:
#         if (len(offerss) and len(cat)):
#             items = ItemMain.objects.filter(category__in = ItemsCat.objects.filter(catName__in=cat), offers__gt=min_off)
#         elif (len(cat)):
#             items = ItemMain.objects.filter(category__in = ItemsCat.objects.filter(catName__in=cat))
#         else:
#             items = ItemMain.objects.filter(offers__gt=min_off)
#     else:
#         items = ItemMain.objects.all()
#     l = []
#     for i in items:
#         ll = []
#         ll.append(ItemsImages.objects.filter(title=ItemMain.objects.filter(title = i.title)[0])[0].image)
#         ll.append(ItemRating.objects.filter(title=ItemMain.objects.filter(title = i.title)[0])[0].ratingValue)
#         ll.append(i.price)
#         ll.append(i.description)
#         ll.append(i.title)
#         price = i.price
#         offer = i.offers
#         newPrice = price - (price * offer)//100
#         ll.append(newPrice)
#         ll.append(i.slug)
#         ll.append(i.offers)
#         l.append(ll)
#     context = {
#         "items": l
#     }
#     return render(request, "products/items_display.html", context)

#@login_required(login_url='login')
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
        itemsearch = list(ItemMain.objects.filter(itemname__icontains = itemname, price = price, discount = discount, expirydate = expirydate))
        if itemsearch == []:
            itemmain = ItemMain.objects.create(
                itemname = itemname,
                discount = discount,
                price = price,
                type = ItemsCat.objects.filter(catName=type)[0],
                quantity = quantity,
                composition = composition,
                manufacturingdate = manufacturingdate,
                expirydate = expirydate
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
            user = User.objects.filter(username = user)[0]
            )
        l = []
        for i in items:
            ll = []
            item =ItemMain.objects.filter(itemid = i.itemid)[0]
            ll.append(i.title)
            ll.append(item.description)
            price = item.price
            discount = item.discount
            newPrice = price - (price * discount)//100
            ll.append(newPrice)
            ll.append(i.total)
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