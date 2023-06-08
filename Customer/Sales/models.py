from django.db import models
from datetime import datetime
import os
from django.contrib.auth.models import User

# from .managers import CustomUserManager
from django.db import models
from django.utils import timezone









####################      Sign Up     ##############################################################

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username
    

############    Remark     ####################################################################    

class Remark(models.Model):
    user = models.CharField(max_length=100)
    customer_id = models.IntegerField()
    datetime = models.DateTimeField(auto_now_add=True)
    reason = models.TextField()

##########    Customer Model  ##################################################################

class Customer(models.Model):
    COMPANY_TYPES = (
        ('new', 'New Client'),
        ('existing', 'Existing Client'),
        ('decline', 'Decline Client'),
    )

    BUSINESS_TYPES = (

        ('manufacturer', 'Manufacturer'),
        ('supplier', 'Supplier'),
        ('trader', 'Trader'),
        ('retail', 'Retail'),
    )

    CLIENT_STATUS = (

        ('prospect', 'Prospect'),
        ('hot_prospect', 'Hot Prospect'),
        ('not_interested', 'Not Interested'),
    )

    company_name = models.CharField(max_length=100)
    type_of_client = models.CharField(max_length=20, choices=COMPANY_TYPES,null=True, blank=True)
    name = models.CharField(max_length=100)
    contact_detail = models.CharField(max_length=100)
    mail_id = models.EmailField()
    nature_of_business = models.CharField(max_length=20, choices=BUSINESS_TYPES,null=True, blank=True)
    meeting_date = models.DateField()
    status_of_client = models.CharField(max_length=20, choices=CLIENT_STATUS,null=True, blank=True)
    next_meeting_date = models.DateField(null=True, blank=True)
    package_sold = models.CharField(max_length=100, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    activation_date = models.DateField(null=True, blank=True)
    renewal_date = models.DateField(null=True, blank=True)

    class Meta:
        db_table = 'Customer'


