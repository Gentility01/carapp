from django.urls import path
from .views import customer_register, mainstaff_register, dashboard, customer_login, mainstaff_login, login_view, logout_view, show_customers

urlpatterns = [
    # path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
     path('dashboard/', dashboard, name='dashboard'),
     path('show_customers/', show_customers, name='show_customers'),
     path('dashboard/', dashboard, name='dashboard'),
     path('customer_login/',customer_login, name='customer_login' ),
     path('customer_register/', customer_register, name='customer_register'),
     path('mainstaff_register/', mainstaff_register, name='mainstaff_register'),
     path('mainstaff_login/', mainstaff_login, name='mainstaff_login'),
    path('logout/', logout_view, name='logout')
]

