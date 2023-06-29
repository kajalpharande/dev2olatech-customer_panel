from django.urls import path
from . import views


urlpatterns = [
    path('customer_list', views.customer_list, name='customer_list'),
    path('show_details/', views.show_details, name='show_details'),
    path('add/', views.add_customer, name='add'),
    path('update/<str:id>/', views.update_customer, name='update'),
    path('delete/', views.Delete, name='delete'),
    path('customer/<int:pk>/',views.Customer_detail, name='customer_detail'),
    path('add_branch/',views.add_branch, name='add_branch'),
    path('branch_list', views.branch_list, name='branch_list'),
    path('add_rm/',views.add_rm, name='add_rm'),
    path('rm_list', views.rm_list, name='rm_list'),
    path('executive_list/', views.executive_list, name='executive_list'),
    path('add_executive/', views.add_executive, name='add_executive'),
    path('get_branch_info/<str:branch>/', views.get_branch_info, name='get_branch_info'),









    #  # START LOGIN URLS
    path('', views.loginPage, name='login_page'),
    path('home/', views.home, name='home'),
    path('logout/', views.logoutUser, name='logout'),
    # END LOGIN URLS


    ######## sign in and sign up url #######

    path('signup/', views.signup, name='signup'),
    # path('signin/', views.signin, name='signin'),
    
    path('create-remark/', views.create_remark, name='create_remark'),
      ################ Forgate password ############
    path('check_email/', views.check_email_exists, name='check_email_exists'),
    path('confirm_password/<int:id>/', views.confirm_password, name='confirm_password'),


 



]


