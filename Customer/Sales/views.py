from django.shortcuts import render,redirect,HttpResponse
from .models import *
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from datetime import datetime
from django.urls import reverse
import json
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from django.utils import timezone
from .models import User, Remark




# @login_required

# def create_remark(request):
#     if request.method == 'POST':
#         reason = request.POST.get('reason')
#         id = request.POST.get('id')
#         username = request.session['username']
#         print(username)
#         date = request.POST.get('datetime')
#         remark = Remark(user=username, reason=reason, customer_id = id,datetime=date)

#         remark.save()
#         return redirect(show_details)

#     return render(request, 'customer_detail.html')

# def show_details(request):
#      customer = get_object_or_404(Customer, pk=id)
#      id = customer.id
#      remark = Remark.objects.filter(customer_id=id)
#      print(remark)
#      context = {
#          'customer': customer,
#          'remark': remark,
#          }
#      return render(request, 'customer_detail.html', context)

def create_remark(request):
    if request.method == 'POST':
        # Retrieve form data
        reason = request.POST.get('reason')
        id = request.POST.get('id')
        username = request.session['username']
        date = request.POST.get('datetime')

        # Save the remark
        remark = Remark(user=username, reason=reason, customer_id=id, datetime=date)
        remark.save()

        # Redirect back to the show_details view with the customer id as a query parameter
        return redirect(f'/show_details/?id={id}')

    return render(request, 'customer_detail.html')

def show_details(request):
    # Retrieve the customer id from the query parameter
    id = request.GET.get('id')
   
    # Retrieve the customer and remarks
    customer = get_object_or_404(Customer, pk=id)
    remark = Remark.objects.filter(customer_id=id)

    context = {
        'customer': customer,
        'remark': remark,
    }
    return render(request, 'customer_detail.html', context)

################ Add Customer data    ########################################

# @login_required(login_url='login_page')
def customer_list(request):
    
    customers = []

    if request.method == 'POST':
       
       customers = request.POST.getlist('customers')

  
    for customer in customers:
            
            customer.url = reverse('customer_detail', args=[customer.pk])
    
    customers = Customer.objects.all()
    context = {
        'customers': customers
    }
    return render(request, 'base.html', context)




#######################    Customer Add   #################################################

def add_customer(request):
    if request.method == 'POST':
        company_name = request.POST.get('company_name')
        type_of_client = request.POST.get('type_of_client')
        name = request.POST.get('name')
        contact_detail = request.POST.get('contact_detail')
        mail_id = request.POST.get('mail_id')
        nature_of_business = request.POST.get('nature_of_business')
        meeting_date = request.POST.get('meeting_date')
        status_of_client = request.POST.get('status_of_client')
        next_meeting_date = request.POST.get('next_meeting_date')
        package_sold = request.POST.get('package_sold')
        amount = request.POST.get('amount')
        activation_date = request.POST.get('activation_date')
        renewal_date = request.POST.get('renewal_date')

        customer = Customer(
            company_name=company_name,
            type_of_client=type_of_client,
            name=name,
            contact_detail=contact_detail,
            mail_id=mail_id,
            nature_of_business=nature_of_business,
            meeting_date=meeting_date,
            status_of_client=status_of_client,
            next_meeting_date=next_meeting_date,
            package_sold=package_sold,
            amount=amount,
            activation_date=activation_date,
            renewal_date=renewal_date
        )
        customer.save()
        return redirect('customer_list') 
    return render(request, 'base.html')



def update_customer(request, id):
    customers = Customer.objects.get(id=id)

    if request.method == 'POST':
        company_name = request.POST.get('company_name')
        type_of_client = request.POST.get('type_of_client')
        name = request.POST.get('name')
        contact_detail = request.POST.get('contact_detail')
        mail_id = request.POST.get('mail_id')
        nature_of_business = request.POST.get('nature_of_business')
        meeting_date = request.POST.get('meeting_date')
        status_of_client = request.POST.get('status_of_client')
        next_meeting_date = request.POST.get('next_meeting_date')
        package_sold = request.POST.get('package_sold')
        amount = request.POST.get('amount')
        activation_date = request.POST.get('activation_date')
        renewal_date = request.POST.get('renewal_date')

        customers = Customer(
            id=id,
            company_name=company_name,
            type_of_client=type_of_client,
            name=name,
            contact_detail=contact_detail,
            mail_id=mail_id,
            nature_of_business=nature_of_business,
            meeting_date=meeting_date,
            status_of_client=status_of_client,
            next_meeting_date=next_meeting_date,
            package_sold=package_sold,
            amount=amount,
            activation_date=activation_date,
            renewal_date=renewal_date
        )
        customers.save()
        return redirect('customer_list') # Replace 'customer_list' with your actual customer list URL name
    return render(request, 'customer_list.html')



def Edit(request):
    customers = Customer.objects.all()
    context = {
        'customers': customers,
    }
    return render(request, 'base.html', context)



def Delete(request):
    if request.method == "POST":
        list_id = request.POST.getlist('id[]')
       
        for i in list_id:
            customers = Customer.objects.filter(id=i).first()
            customers.delete()
 
    return redirect('customer_list')



################# customer detail page ################################


def Customer_detail(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    id = customer.id
    remark = Remark.objects.filter(customer_id=id)
   
    context = {
        'customer': customer,
        'remark': remark,
    }
    return render(request, 'customer_detail.html', context)






##################  Home Page #######################################


def home(request):
    
    customer_count = Customer.objects.all()
    
    context={
        'customer_count':len(customer_count),
    
    }
    return render(request,'base.html',context)
    
    
#############  Login Page ########################################################


def loginPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        request.session['username'] = username
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
            if password == user.password:
                # Authentication successful, proceed with further actions
                return redirect('customer_list')  # Replace 'customer_list' with your desired URL or view name
            else:
                error_message = "Invalid username or password."
        except User.DoesNotExist:
            error_message = "Invalid username or password."
        
        return render(request, 'login.html', {'error_message': error_message})

    return render(request, 'login.html')






def logoutUser(request):
    logout(request)
    return render(request,'login.html')


########### sign up ####################################

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User(username=username,  password=password)
        user.save()
        return redirect('login_page')
    return render(request, 'signup.html')

