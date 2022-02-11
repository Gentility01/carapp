from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Category, Product #CustomUser, MainAdmin, CustomerAdmin

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
# admin.site.register(CustomUser, UserAdmin)
# admin.site.register(MainAdmin)
# admin.site.register(CustomerAdmin)
