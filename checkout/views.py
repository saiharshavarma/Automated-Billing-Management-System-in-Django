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
#             Bfirst_name = request.POST['Bfirst_name']
#             Blast_name = request.POST['Blast_name']
#             Bcheckout_states = Bstates.objects.get(states = request.POST['Bstates'])
#             Bstreet = request.POST['Bstreet']
#             Bapartment = request.POST['Bapartment']
#             Bcity = request.POST['Bcity']
#             Bzip = request.POST['Bzip']
#             Bphone = request.POST['Bphone']
#             Bemail = request.POST['Bemail']    
#             cardno = request.POST['cardno']
#             namecard = request.POST['namecard']
#             validity = request.POST['validity']
#             cvv = request.POST['cvv']
#             billing = Billing.objects.create(Bfirst_name=Bfirst_name, Blast_name=Blast_name, Bcheckout_states=Bcheckout_states, Bstreet=Bstreet, Bapartment=Bapartment, Bcity=Bcity, Bzip=float(Bzip), Bphone=float(Bphone), Bemail=Bemail)
#             shipping = Shipping.objects.create(Sfirst_name=Bfirst_name, Slast_name=Blast_name, Scheckout_states=Bcheckout_states, Sstreet=Bstreet, Sapartment=Bapartment, Scity=Bcity, Szip=Bzip, Sphone=Bphone, Semail=Bemail)
#             payment = Payment.objects.create(cardno=cardno, namecard=namecard, validity=validity, cvv=cvv)
#             billing.save()
#             payment.save()
#             shipping.save()        
#             return render(request, 'success.html')
#         else:
#             return redirect('login')
#     else:
#         return render(request, 'checkout.html', context)    