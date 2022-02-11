from django.http import request
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth import login, logout
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views.generic import CreateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# from home.EmailBackEnd import EmailBackEnd
from django.contrib import messages
from django.db.models import Count

from .models import Product, Category
from .forms import ProductCreateForm, CategoryCreateForm




def product_list(request):
    products = Product.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(products, 2)
    try:
        p_pages = paginator.page(page)
    except PageNotAnInteger:
        p_pages = paginator.page(1)
    except EmptyPage:
        p_pages = paginator.page(paginator.num_pages)
        
    categories = Category.objects.all()
    categories = Category.objects.all().annotate(posts_count=Count('product')) 
    for category in categories:
        print(category.posts_count)
        
    # product_paginator = Paginator(product, 4)
    # page_num = request.GET.get('page')
    # page = product_paginator.get_page(page_num)
    
    # if category_slug:
    #     category = get_object_or_404(Category, slug=category_slug)
    #     product = product.filter(category=category)
        

        
    context = {
            'page':page,
            'p_pages':p_pages,
            'categories':categories
        }
    return render(request, 'home/article_list.html', context)
    
    
def product_detail(request, id):
    product  = get_object_or_404(Product, id=id)
    context = {
        'product':product
    }
    return render(request, 'home/productdetail.html', context)


def  create_post(request):
    form = ProductCreateForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = ProductCreateForm()
    context = {
        'form':form
    }
    return render(request,'home/product_create.html', context)

def category_post(request):
    c_form = CategoryCreateForm(request.POST or None)
    if c_form.is_valid():
        c_form.save()
        c_form = CategoryCreateForm()
    context = {
        'c_form':c_form
    }
    return render(request,'home/product_create.html', context)

 
 
 # this is where the error is coming from
def category_list(request, id):
    categories = Category.objects.all()
    
    products = Product.objects.filter()
    
    if category_slug:
       category =get_object_or_404(Category, i)
       products = products.filter(category=category)    
    
    context = {
        'categories':categories,
         'products':products,
        'category':category
      
        
    }
    return render(request, 'home/category.html', context)
    