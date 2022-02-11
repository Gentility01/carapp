# from django.db import models
# from django.contrib.auth.models import AbstractUser
# # Create your models here.


# Gender = (
#     ('M','Male') ,   # first entry goes into the database and thr second entry does into the template
#     ('F','Female'),
   
# )

# class CustomUser(AbstractUser):
#     user_type_data = ((1,"HOD"), (2,"Staff"), (3,"Student"))  #setting a tuple for the admins 1 for Admin, 2 for Staffs and 3 for Student 
#     user_type = models.CharField(default = 1, choices = user_type_data, max_length=10)


# class MainAdmin(models.Model):
#     id        = models.AutoField(primary_key=True)
#     name      = models.CharField( max_length=100)
#     email     = models.EmailField( max_length=254)
#     password  = models.CharField( max_length=200)
#     gender    = models.CharField(choices=Gender, max_length=1)
#     picture   = models.ImageField()
    
    
    
# class CustomerAdmin(models.Model):
#     id        = models.AutoField(primary_key=True)
#     name      = models.CharField( max_length=100)
#     email     = models.EmailField( max_length=254)
#     password  = models.CharField( max_length=200)
#     gender    = models.CharField(choices=Gender, max_length=1)
#     picture   = models.ImageField()
    