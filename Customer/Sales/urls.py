from django.urls import path
from . import views

urlpatterns = [
    path('customer_list', views.customer_list, name='customer_list'),
    path('add/', views.add_customer, name='add'),
    path('update/<str:id>/', views.update_customer, name='update'),
    path('delete/', views.Delete, name='delete'),
    path('customer/<int:pk>/',views.Customer_detail, name='customer_detail'),



    #  # START LOGIN URLS
    path('login', views.loginPage, name='login_page'),
    path('home/', views.home, name='home'),
    path('logout/', views.logoutUser, name='logout'),
    # END LOGIN URLS


    ######## sign in and sign up url #######

    path('', views.signup, name='signup'),
    # path('signin/', views.signin, name='signin'),
    
    path('create-remark/', views.create_remark, name='create_remark'),


 

################          user Roles   ######################################################################


#   path('logs/', views.view_logs, name='view_logs'),
#     path('logs/delete/', views.LogsDelete, name='logs_delete'),
#     path('roles/', views.role_display, name='role_display'),
#     path('roles/add/', views.role_add, name='role_add'),
#     path('users/', views.user_display, name='user_display'),
#     path('users/new/', views.add_new_user, name='add_new_user'),
#     path('users/<int:id>/edit/', views.user_edit, name='user_edit'),
#     path('users/get_Existing_user/', views.get_Existing_user, name='get_Existing_user'),



]


