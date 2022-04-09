# from typing import AnyStr
# from django.contrib.auth.models import User
# from django.shortcuts import redirect, render
# from .models import ItemMain, ItemsCat, ItemsImages, ItemRating, ItemsSpecifications, ItemFaq, UserCart, Billing, Payment, Shipping, ItemMain
# import json
# from django.contrib.auth.decorators import login_required

# # Create your views here.
# @login_required(login_url='login')
# def checkout(request):
#     if request.method == 'GET':
#         user = request.user
#         items = UserCart.objects.filter(
#             user = User.objects.filter(username = user)[0]
#             )
#         l = []
#         sprice = 0
#         snewPrice = 0
#         for i in items:
#             ll = []
#             item =ItemMain.objects.filter(title = i.title)[0]
#             price = item.price
#             offer = item.offers
#             newPrice = price - (price * offer)//100

#             sprice += price
#             snewPrice += newPrice
#         context = {}
#         context['price'] = sprice
#         context['offer'] = sprice - snewPrice
#         context['newPp'] = snewPrice
        
#     if request.method == 'POST':
#         if request.user.is_authenticated:
#             first_name = request.POST['first_name']
#             middle_name = request.POST['middle_name']
#             last_name = request.POST['last_name']
#             states = request.POST['states']
#             street = request.POST['street']
#             city = request.POST['city']
#             phone = request.POST['phone']
#             email = request.POST['email']    
#             billing = Billing.objects.create(first_name=first_name, middle_name=middle_name, last_name=last_name, states=states, street=street, city=city, phone=float(phone), email=email)
#             billing.save()      
#             return render(request, 'success.html')
#         else:
#             return redirect('login')
#     else:
#         return render(request, 'checkout.html', context)    