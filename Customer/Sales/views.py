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
from .models import Users, Remark
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render






def create_remark(request):
    if request.method == 'POST':
        # Retrieve form data
        reason = request.POST.get('reason')
        id = request.POST.get('id')
        username = request.session['username']

        now = datetime.now()

        # Save the remark
        remark = Remark(user=username, reason=reason, customer_id=id, datetime=now)
        remark.save()

        # Redirect back to the show_details view with the customer id as a query parameter
        return redirect(f'/show_details/?id={id}')

    return render(request, 'customer_detail.html')


def show_details(request):
    # Retrieve the customer id from the query parameter
    id = request.GET.get('id')
    executives = cl_Executive.objects.all()
    branches = cl_Branch.objects.all() 
    rm1 = cl_Manager.objects.all()
    
    # Retrieve the customer and remarks
    customer = get_object_or_404(Customer, pk=id)
    remark = Remark.objects.filter(customer_id=id)

    context = {
        'customer': customer,
        'remark': remark,
        'executives':executives,
        'branches':branches,
        'rm1':rm1

    }
    return render(request, 'customer_detail.html', context)

################         Add Customer data    ########################################

# @login_required(login_url='login_page')
def customer_list(request):
    executives = cl_Executive.objects.all()
    branches = cl_Branch.objects.all() 
    rm1 = cl_Manager.objects.all()
    
    customers = []

    if request.method == 'POST':
       
       customers = request.POST.getlist('customers')

  
    for customer in customers:
            
            customer.url = reverse('customer_detail', args=[customer.pk])
    
    customers = Customer.objects.all()
    context = {
        'customers': customers,
        'executives':executives,
        'branches':branches,
        'rm1':rm1
    }
    return render(request, 'base.html', context)




#######################    Customer Add   #################################################

def add_customer(request):
    if request.method == 'POST':
        e_name = request.POST.get("e_name")

        branch_list = request.POST.get('branch_list')
        manager_name = request.POST.get('manager_name')

        ex_name = request.POST.get('ex_name')


        company_name = request.POST.get('company_name')
        type_of_client = request.POST.get('type_of_client')
        name = request.POST.get('name')
        contact_detail = request.POST.get('contact_detail')
        mail_id = request.POST.get('mail_id')
        # nature_of_business = request.POST.get('nature_of_business')
        meeting_date = request.POST.get('meeting_date')
        # status_of_client = request.POST.get('status_of_client')
        next_meeting_date = request.POST.get('next_meeting_date')
        # package_sold = request.POST.get('package_sold')
        amount = request.POST.get('amount')
        activation_date = request.POST.get('activation_date')
        renewal_date = request.POST.get('renewal_date')

        customer = Customer(
            branch_list=branch_list,
            manager_name =manager_name,

            ex_name=ex_name,
            company_name=company_name,
            type_of_client=type_of_client,
            name=name,
            contact_detail=contact_detail,
            mail_id=mail_id,
            # nature_of_business=nature_of_business,
            meeting_date=meeting_date,
            # status_of_client=status_of_client,
            next_meeting_date=next_meeting_date,
            # package_sold=package_sold,
            amount=amount,
            activation_date=activation_date,
            renewal_date=renewal_date
        )
        customer.save()
        name = e_name
        return redirect('executive_dash', name = name) 
    return render(request, 'exe_sale.html')



def update_customer(request, id):

    customers = Customer.objects.get(id=id)
    executives = cl_Executive.objects.all()
    branches = cl_Branch.objects.all() 
    rm1 = cl_Manager.objects.all()
    context = {
        'customers': customers,
        'executives':executives,
        'branches':branches,
        'rm1':rm1
    }

    if request.method == 'POST':
       
        branch_name = request.POST.get('branch_name')
        manager_name = request.POST.get('manager_name')

        ex_name = request.POST.get('ex_name')
        company_name = request.POST.get('company_name')
        type_of_client = request.POST.get('type_of_client')
        name = request.POST.get('name')
        contact_detail = request.POST.get('contact_detail')
        mail_id = request.POST.get('mail_id')
        # nature_of_business = request.POST.get('nature_of_business')
        meeting_date = request.POST.get('meeting_date')
        # status_of_client = request.POST.get('status_of_client')
        next_meeting_date = request.POST.get('next_meeting_date')
        # package_sold = request.POST.get('package_sold')
        amount = request.POST.get('amount')
        activation_date = request.POST.get('activation_date')
        renewal_date = request.POST.get('renewal_date')

        customers = Customer(
            id=id,
            branch_list = branch_name,
            manager_name =manager_name,

            ex_name=ex_name,
            company_name=company_name,
            type_of_client=type_of_client,
            name=name,
            contact_detail=contact_detail,
            mail_id=mail_id,
            # nature_of_business=nature_of_business,
            meeting_date=meeting_date,
            # status_of_client=status_of_client,
            next_meeting_date=next_meeting_date,
            # package_sold=package_sold,
            amount=amount,
            activation_date=activation_date,
            renewal_date=renewal_date
        )
        
        customers.save()
        return redirect('customer_list') # Replace 'customer_list' with your actual customer list URL name
    return render(request, 'customer_detail.html',context)



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
    executives = cl_Executive.objects.all()
    branches = cl_Branch.objects.all() 
    rm1 = cl_Manager.objects.all()
   
    context = {
        'customer': customer,
        'remark': remark,
        'executives':executives,
        'branches':branches,
        'rm1':rm1
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


# def loginPage(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         request.session['username'] = username
#         password = request.POST['password']
#         try:
#             user = Users.objects.get(username=username)
#             if password == user.password:
#                 if user.roles == 'Admin':
#                     return redirect('customer_list')
#                 elif user.roles == 'Manager':
#                     name = user.name
#                     return redirect('manager_dash', name = name)  
#                 elif user.roles == 'Executive':
#                     name = user.name
#                     return redirect('executive_dash',name =name)
                
#             else:
#                 error_message = "Invalid username or password."
#         except Users.DoesNotExist:
#             error_message = "Invalid username or password."
        
#         return render(request, 'login.html', {'error_message': error_message})

#     return render(request, 'login.html')

def loginPage(request):
    
    if request.method == 'POST':

        username = request.POST['username']

        request.session['username'] = username

        password = request.POST['password']

        try:

            user = Users.objects.get(username=username)

            if password == user.password:

                if user.roles == 'Admin':

                    return redirect('customer_list')

                elif user.roles == 'Manager':

                    name = user.name

                    return redirect('manager_dash', name=name)  

                elif user.roles == 'Executive':

                    name = user.name

                    return redirect('executive_dash', name=name)

            else:

                error_message = "Invalid username or password."

        except Users.DoesNotExist:

            try:

                manager = cl_Manager.objects.get(username=username)

                if password == manager.password:

                    name = manager.manager_name

                    return redirect('manager_dash', name=name)

                else:

                    error_message = "Invalid username or password."

            except cl_Manager.DoesNotExist:

                try:

                    executive = cl_Executive.objects.get(username=username)

                    if password == executive.password:

                        name = executive.ex_name

                        return redirect('executive_dash', name=name)

                    else:

                        error_message = "Invalid username or password."

                except cl_Executive.DoesNotExist:

                    error_message = "Invalid username or password."

                    

        return render(request, 'login.html', {'error_message': error_message})




    return render(request, 'login.html')




def logoutUser(request):
    logout(request)
    return redirect("login_page")


###########################    sign up    ###################################

# def signup(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = User(username=username,  password=password)
#         user.save()
#         return redirect('login_page')
#     return render(request, 'signup.html')


# def signup(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
        
#         # Check if the username already exists
#         if User.objects.filter(username=username).exists():
#             error_message = "Username already exists."
#             return render(request, 'signup.html', {'error_message': error_message})
        
#         # Create a new user
#         user = User(username=username, password=password)
#         user.save()
#         return redirect('login_page')
    
#     return render(request, 'signup.html')

def signup(request):
    if request.method == 'POST':
        email = request.POST['username']
        password = request.POST['password']

        # Extract the username from the email
        username = email.split('@')[0]

        # Check if the email is from the allowed domain
        if not email.endswith('@olatechs.com'):
            error_message = "Only users with Olatech email addresses are allowed to register."
            return render(request, 'signup.html', {'error_message': error_message})

        # Check if the username already exists
        if Users.objects.filter(username=username).exists():
            error_message = "Username already exists."
            return render(request, 'signup.html', {'error_message': error_message})

        # Create a new user
        user = Users(username=email, password=password)
        user.save()
        return redirect('login_page')

    return render(request, 'signup.html')



def check_email_exists(request):
    if request.method == 'POST':
        email = request.POST.get("username")
        
        # Check if the email exists in the database
        try:
            user = Users.objects.get(username=email)
        except Users.DoesNotExist:
            messages.error(request, "Email address does not exist.")
            return redirect('check_email_exists')
        
        return redirect('confirm_password', id=user.id)
    
    return render(request, 'forgot_password.html')



def confirm_password(request,id):
    print(id)
    if request.method == 'POST':
        # Retrieve the user object using the user ID from session
     
        
        try:
            user = Users.objects.get(id=id)
        except Users.DoesNotExist:
            messages.error(request, "Invalid password reset link.")
            return redirect('forgot_password')
        
        # Get the new password and confirm password from the form
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        
        if new_password == confirm_password:
            # Set the new password for the user
            user.password=new_password
            user.save()
            
            # Clear the reset UID and token from session
           
            
            messages.success(request, "Password reset successful. You can now log in with your new password.")
            return redirect('login_page')
        else:
            messages.error(request, "Passwords do not match.")
    
    return render(request, 'confirm_password.html')



############### Branch ###############################################

def branch_list(request):
    branch = cl_Branch.objects.all()
    return render(request, 'branch.html', {'branches': branch})



def add_branch(request):
    if request.method == 'POST':
        branch_name = request.POST.get('branch_name')
        branch = cl_Branch(branch_name=branch_name)
        branch.save()
        return redirect('branch_list')
    branches = cl_Branch.objects.all()  # Fetch all branches
    return render(request, 'branch.html', {'branches': branches})





def update_branch(request, id):
    
    branches = cl_Branch.objects.get(id=id)

    if request.method == 'POST':
        branch_name = request.POST.get('branch_name')
        
        branches = cl_Branch(
            id=id,
            branch_name=branch_name,
            
        )
        branches.save()
        return redirect('branch_list')
    return render(request, 'branch.html')




##############  RM ###############################

def manager_list(request):
    rm = cl_Manager.objects.all()
    branches = cl_Branch.objects.all() 
    user = User.objects.all 

    return render(request, 'rm.html', {'rm1': rm, 'branches': branches,'user':user})


def add_rm(request):
    if request.method == 'POST':
        manager_name = request.POST.get('manager_name')
        branch_list = request.POST.get('branch_list')
        username = request.POST.get('username')
        password = request.POST.get('password')
       


        rm = cl_Manager(
            manager_name=manager_name,
            branch_list=branch_list,
            username =  username,
            password =password
            )
        rm.save()
        return redirect('manager_list')
    rm1 = cl_Manager.objects.all()  # Fetch all RM
    return render(request, 'rm.html', {'rm1': rm1})




def update_rm(request, id):

    rm1 = cl_Manager.objects.get(id=id)

    if request.method == 'POST':
        manager_name = request.POST.get('manager_name')
        branch_list = request.POST.get('branch_list')        
        username = request.POST.get('username')        
        password = request.POST.get('password')        
        rm1 = cl_Manager(
            id=id,
            manager_name=manager_name,
            branch_list=branch_list,
            username=username,
            password=password,
            
        )
        rm1.save()
        return redirect('manager_list')
    return render(request, 'rm.html')




######################   Executive  ############################################################

def executive_list(request):
    executives = cl_Executive.objects.all()
    branches = cl_Branch.objects.all()  # Fetch all branches
    rm1 = cl_Manager.objects.all()
    user = User.objects.all 



    return render(request, 'executive.html', {'executives': executives,'branches':branches,'rm1':rm1,'user':user})


def add_executive(request):
    if request.method == 'POST':
        ex_name = request.POST.get('ex_name')
        # manager_list = request.POST.get('manager_list')

        branch_list = cl_Branch.objects.filter(branch_name=request.POST.get('branch_list')).first()
        manager_name = request.POST.get('manager_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
       

        executive = cl_Executive(
            ex_name=ex_name, 
            branch_list=branch_list, 
            manager_name=manager_name,
            username =  username,
            password =password
            )
        executive.save()

        return redirect('executive_list')

    branches = cl_Branch.objects.all()
    rm1 = cl_Manager.objects.all()
    executives = cl_Executive.objects.all()

    return render(request, 'executive.html', {'branches': branches, 'rms': rm1,'executives':executives})




def update_executive(request, id):
    print(id)
    executives = cl_Executive.objects.get(id=id)

    if request.method == 'POST':
        
        ex_name = request.POST.get('ex_name')
        branch_list = cl_Branch.objects.filter(branch_name=request.POST.get('branch_list')).first()
        manager_name = request.POST.get('manager_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

       
        executives = cl_Executive(
            id=id,
            ex_name=ex_name,
            branch_list=branch_list,
            manager_name=manager_name,
            username=username,
            password=password


            
        )
        executives.save()
        return redirect('executive_list')
    return render(request, 'executive.html')





######## GET RM BY BRANCH ##############################################


def get_branch_info(request,branch):
    branchi = cl_Manager.objects.get(branch_list = branch)

    
    branchi_info = {
        'manager': branchi.manager_name,
    
        }
    return JsonResponse(branchi_info)


############# ROLES #####################################

def role_display(request):
    roles = Roles.objects.all()
    return render(request, 'roles.html', {'roles': roles})
   


def add_role(request):
    if request.method == 'POST':
        role_name = request.POST.get('role_name')
        branch = Roles(role_name=role_name)
        branch.save()
        return redirect('role_display')
    roles = Roles.objects.all()  # Fetch all branches
    return render(request, 'roles.html', {'roles': roles})



##########   User Create   ###################################################


def user_list(request):
    roles =Roles.objects.all()

    users = Users.objects.all()
    return render(request, 'users.html', {'users': users,'roles':roles})






def register_user(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        roles = request.POST.get('roles')

        user = Users(name=name, username=username, email=email, password=password, roles=roles)
        user.save()
        return redirect('user_list')

    return render(request, 'users.html')


############ Manager  and Executives Leads ###########################################################3

def manager_dash(request, name):
    rm = Customer.objects.filter(manager_name=name)
    branches = cl_Branch.objects.all() 
    executives = cl_Executive.objects.filter(manager_name=name)

    return render(request,'manager_sales.html', {'rm1': rm, 'branches': branches,'executives':executives})




def executive_dash(request, name):
    request.session['exe_name'] = name
    print("hhhhh",name)
    executives = cl_Executive.objects.all()
    branches = cl_Branch.objects.all()  # Fetch all branches
    rm1 = cl_Manager.objects.all()
    exe_list = Customer.objects.filter(ex_name = name)
    e_name = name
    cl_ex = cl_Executive.objects.filter(ex_name = e_name)
    for i in cl_ex:
        print(i.manager_name)
    return render(request, 'exe_sale.html', {'executives': executives,'branches':branches,'rm1':rm1,'exe_list': exe_list,'name':request.session['exe_name'],'e_name':e_name,"cl_ex":cl_ex})