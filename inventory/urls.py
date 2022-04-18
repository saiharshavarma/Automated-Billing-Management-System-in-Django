from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="homepage"),
    path('view', views.items_display, name="view"),
    path('upload_item', views.item_upload, name="inventoryadd"),
    path('cart', views.cart, name="cart"),
    path('clear_cart', views.clear_cart, name='clear_cart'),
    path('empty_cart', views.empty_cart, name='empty_cart'),
    path('contact', views.contact, name="contact"),
    path('about', views.about, name="about"),
    path('t&c', views.tnc, name="tnc")
]
