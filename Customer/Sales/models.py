from django.db import models
from datetime import datetime
import os
from django.contrib.auth.models import User

# from .managers import CustomUserManager
from django.db import models
from django.utils import timezone










####################      Sign Up     ##############################################################

class Users(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField(default="abc@olatechs.com")
    password = models.CharField(max_length=100)
    roles = models.CharField(max_length=100)

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
        ('po', 'PO Recieved'),

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
    manager_name = models.CharField(max_length=100 )
    branch_list = models.CharField(max_length=100 ) 
    ex_name = models.CharField(max_length=100 )

    company_name = models.CharField(max_length=100)
    type_of_client = models.CharField(max_length=20, choices=COMPANY_TYPES,null=True, blank=True)
    name = models.CharField(max_length=100)
    contact_detail = models.CharField(max_length=100)
    mail_id = models.EmailField()
    # nature_of_business = models.CharField(max_length=20, choices=BUSINESS_TYPES,null=True, blank=True)
    meeting_date = models.DateField()
    # status_of_client = models.CharField(max_length=20, choices=CLIENT_STATUS,null=True, blank=True)
    next_meeting_date = models.DateField(null=True, blank=True)
    # package_sold = models.CharField(max_length=100, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    activation_date = models.DateField(null=True, blank=True)
    renewal_date = models.DateField(null=True, blank=True)

    class Meta:
        db_table = 'Customer'

#####################  Branch #######################################################

class cl_Branch(models.Model):
    branch_name = models.CharField(max_length=100)

    class Meta:
        db_table ='Branch'

############## Manager ################################################3


class cl_Manager(models.Model):
    manager_name = models.CharField(max_length=100)
    branch_list = models.CharField(max_length=100) 
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    


    class Meta:
        db_table ='RM'


########## EXecutive #############################################

class cl_Executive(models.Model):
    ex_name = models.CharField(max_length=100)
    branch_list = models.ForeignKey ( cl_Branch, on_delete=models.CASCADE, null=True, blank=True) 
    manager_name =  models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    class Meta:
        db_table ='executive'


############# USR ROLE ##################################

class Roles(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    role_name=models.CharField(max_length = 200, unique=True)

    class Meta:
        db_table = 'Roles'
