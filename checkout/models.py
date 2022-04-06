# from django.db import models

# # Create your models here.

# class Billing(models.Model):
#     Bfirst_name = models.CharField(max_length= 264)
#     Blast_name = models.CharField(max_length= 264)
#     Bstreet = models.CharField(max_length= 264)
#     Bapartment = models.CharField(max_length= 264)
#     Bcity = models.CharField(max_length= 264)
#     Bzip = models.IntegerField(default=0)
#     Bphone = models.IntegerField(default=0)
#     Bemail = models.EmailField(max_length= 264)

# class Shipping(models.Model):
#     Sfirst_name = models.CharField(max_length= 264)
#     Slast_name = models.CharField(max_length= 264)
#     Sstreet = models.CharField(max_length= 264)
#     Sapartment = models.CharField(max_length= 264)
#     Scity = models.CharField(max_length= 264)
#     Szip = models.IntegerField(default=0)
#     Sphone = models.IntegerField(default=0)
#     Semail = models.EmailField(max_length= 264)

# class Payment(models.Model):
#     cardno = models.IntegerField(default=0)
#     namecard = models.CharField(max_length= 264)
#     cvv = models.IntegerField(default=0)
#     validity = models.DateField(default="0000-00")

#     def save(self, *args, **kwargs):
#         check = self.validity.split("-")
#         print(check)
#         if len(check) == 2:
#             self.validity += "-01"
#             print(self.validity)
#         super().save(*args, **kwargs)
