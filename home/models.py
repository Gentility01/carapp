from django.db import models
from django.urls import reverse
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField



# Gender = (
#     ('M','Male') ,   # first entry goes into the database and thr second entry does into the template
#     ('F','Female'),
   
# )

# class CustomUser(AbstractUser):
#     user_type_data = ((1,"MainAdmin"), (2,"CustomerAdmin"))  #setting a tuple for the admins 1 for Admin, 2 for Staffs and 3 for Student 
#     user_type = models.CharField(default = 1, choices = user_type_data, max_length=10)
    
    
# class MainAdmin(models.Model):
#     id        = models.AutoField(primary_key=True)
#     admin     = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
#     gender    = models.CharField(choices=Gender, max_length=1)
#     picture   = models.ImageField()
#     # customer  = models.ForeignKey('CustomerAdmin', on_delete=models.CASCADE)
#     # product  = models.ForeignKey('Product', on_delete=models.CASCADE)
#     # category  = models.ForeignKey('Category', on_delete=models.CASCADE)
#     dateposted= models.DateField(auto_now_add=True)
#     dateupdated= models.DateField(auto_now_add=True)
    
    
    
# class CustomerAdmin(models.Model):
#     id        = models.AutoField(primary_key=True)
#     # name      = models.CharField( max_length=100)
#     # email     = models.EmailField( max_length=254)
#     admin     = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
#     # password  = models.CharField( max_length=200)
#     gender    = models.CharField(choices=Gender, max_length=1)
#     picture   = models.ImageField()
#     country = CountryField()
#     dateposted= models.DateField(auto_now_add=True)
#     dateupdated= models.DateField(auto_now_add=True)
    
    
        
    
    
# Create your models here.
class Category(models.Model):
    name   = models.CharField( max_length=100)
    slug   = models.SlugField(unique=True)
    
    class Meta:
        ordering = ('name',)
    
    def __str__(self):
        return self.name
    
    
    def get_absolute_url(self):
        return reverse('product:category', args=[self.slug])
    


class Product(models.Model):
    name           = models.CharField( max_length=100)
    image          = models.ImageField(upload_to = 'pictures/', blank = True, null = True,)
    price          = models.FloatField()
    category       = models.ForeignKey(Category, on_delete=models.CASCADE)   
    date_created   = models.DateTimeField( auto_now=True) 
    discount_price =  models.FloatField()
    description    =models.TextField()
    
    def get_absolute_url(self):
        return reverse("product:category", args={ self.category.name})
    
    
    
    
    class Meta:
        
        ordering = ('-id',)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("product:product_detail", args=[self.id])
    
    
    


# @receiver(post_save, sender=CustomUser)
# def create_user_profile(sender,instance, created, **kwargs):
#     if created:
#         if instance.user_type==1:
#             MainAdmin.objects.create(admin=instance)
            
#         if instance.user_type==2:
#             CustomerAdmin.objects.create(admin=instance)
            
            
# @receiver(post_save, sender=CustomUser)
# def save_user_profile(sender, instance,  **kwargs):
    
#     if instance.user_type==1:
#         instance.mainadmin.save()
        
#     if instance.user_type==2:
#         instance.customadmin.save()
    

    


