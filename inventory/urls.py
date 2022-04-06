from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="homepage"),
    path('upload_item', views.item_upload, name="inventoryadd"),
]