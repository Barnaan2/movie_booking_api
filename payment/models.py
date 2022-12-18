from django.db import models
from user.models import Profile
from booking.models import BookingRequest
from system_admin.models import Cinema

class PaymentMethod(models.Model):
    name = models.CharField(max_length=55,null=True,blank=True)
    type = models.CharField(max_length=55,null=True,blank=True)
    short_code = models.CharField(max_length=20,null=True,blank=True)
    company_logo = models.ImageField(null=True,blank=True, default='payment_method.png')
    description = models.TextField(max_length=200,null=True,blank=True)
    contact = models.CharField(max_length=20,null=True,blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created', '-updated')
 

        

    def __str__(self):
        return str(self.name)
    
class PaymentInformation(models.Model):
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE,null=True,blank=True)
    added_by = models.ForeignKey(Profile, on_delete=models.CASCADE,null=True,blank=True)
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.CASCADE,null=True,blank=True)
    account_holder = models.CharField(max_length=100,null=True,blank=True)
    account_number = models.CharField(max_length=50,null=True,blank=True)
    verified = models.BooleanField(default=False, null=True,blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
            ordering = ('-created', '-updated')
            unique_together = [['cinema', 'payment_method']]

    def __str__(self):
        return str(self.account_number)


class Paid(models.Model):
    booking_request = models.OneToOneField(BookingRequest,on_delete=models.CASCADE,null=True,blank=True)
    payment_info = models.ForeignKey(PaymentInformation,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=50,null=True,blank=True)
    transaction_id = models.CharField(max_length=100,null=True,blank=True)
    picture = models.ImageField(null=True,blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
            ordering = ('-created', '-updated')
            unique_together = [['booking_request', 'payment_info','transaction_id']]

    def __str__(self):
        return str(self.transaction_id)