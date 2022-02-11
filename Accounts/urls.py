from django.urls import path
from .views import customer_register, mainstaff_register, dashboard, customer_login #register_view, login_view

urlpatterns = [
    # path('register/', register_view, name='register'),
    # path('login/', login_view, name='login'),
     path('dashboard/', dashboard, name='dashboard'),
     path('customer_login/',customer_login, name='customer_login' ),
     path('customer_register/', customer_register, name='customer_register'),
     path('mainstaff_register/', mainstaff_register, name='mainstaff_register'),
    # path('logout/', logout_view, name='logout')
]

