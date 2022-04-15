from time import timezone
from django.db import models
from inventory.models import ItemMain, User
import datetime
# Create your models here.


class CustomerDetails(models.Model):
    customerid = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=264)
    middle_name = models.CharField(max_length=264)
    last_name = models.CharField(max_length=264)
    street = models.CharField(max_length=264)
    state = models.CharField(max_length=264)
    city = models.CharField(max_length=264)
    phone = models.IntegerField(default=0)
    email = models.EmailField(max_length=264)

    def __str__(self) -> str:
        return str("Customer ID: " + str(self.customerid) + " -> Customer Name: " + str(self.first_name))


class Medicine_Logs(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    customer = models.ForeignKey(CustomerDetails, on_delete=models.PROTECT)
    itemid = models.ForeignKey(ItemMain, on_delete=models.PROTECT)
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(decimal_places=2, max_digits=25)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(str(self.date) + " -> Operator: " + str(self.user) + " -> Item: " + str(self.itemid) + " -> " + str(self.customer))
