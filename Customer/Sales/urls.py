from django.urls import path
from . import views


urlpatterns = [
    ############ Customer Lead Data ############################

    path('customer_list', views.customer_list, name='customer_list'),
    path('show_details/', views.show_details, name='show_details'),
    path('add/', views.add_customer, name='add'),
    path('update/<str:id>/', views.update_customer, name='update'),
    path('delete/', views.Delete, name='delete'),
    path('customer/<int:pk>/',views.Customer_detail, name='customer_detail'),
    path('create-remark/', views.create_remark, name='create_remark'),


    ############  Branch ########################################

    path('add_branch/',views.add_branch, name='add_branch'),
    path('branch_list', views.branch_list, name='branch_list'),
    path('update_branch/<str:id>', views.update_branch, name='update_branch'),

    ########### RM ##################################################
    path('add_rm/',views.add_rm, name='add_rm'),
    path('manager_list', views.manager_list, name='manager_list'),
    path('update_rm/<str:id>', views.update_rm, name='update_rm'),

    ########### Executive #####################################################

    path('executive_list', views.executive_list, name='executive_list'),
    path('add_executive/', views.add_executive, name='add_executive'),
    path('get_branch_info/<str:branch>/', views.get_branch_info, name='get_branch_info'),
    path('update_executive/<str:id>', views.update_executive, name='update_executive'),

    ######### Roles ########################################3
    path('add_role/', views.add_role, name='add_role'),

    path('role_display/',views.role_display, name='role_display'),


    ############## Register  Users ############################
    path('register_user/',views.register_user, name='register_user'),
    path('user_list/', views.user_list, name='user_list'),



  ##### START LOGIN URLS #####################

    path('', views.loginPage, name='login_page'),
    path('home/', views.home, name='home'),
    path('logout/', views.logoutUser, name='logout'),
    # END LOGIN URLS


    ######## sign in and sign up url #######

    path('signup/', views.signup, name='signup'),
    # path('signin/', views.signin, name='signin'),
    
      ################ Forgate password ############

    path('check_email/', views.check_email_exists, name='check_email_exists'),
    path('confirm_password/<int:id>/', views.confirm_password, name='confirm_password'),


    path('manager_dash/<str:name>/', views.manager_dash, name='manager_dash'),

    path('executive_dash/<str:name>/',views.executive_dash, name='executive_dash'),

 



]


