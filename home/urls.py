from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    # home_view,
    # login_page,
    product_list,
    product_detail,
    create_post,
    category_post,
    CategoryListView,
    # category_list
    # login_page,
    # doLogin,
    # GetUserDetail,
    # logout_user,
    
    # ProductCreateView 
    
)

app_name = 'product'

urlpatterns = [
    # path('', home_view, name='homeview'),
    # path('product_create', ProductCreateView.as_view(), name='product_create'),
    path('home/', product_list, name='product_list'),
    # path('', login_page, name='login'),
    # path('doLogin', doLogin, name='doLogin'),
    # path('get_user_details/', GetUserDetail, name='get_user_detail'),
    # path('logout_user', logout_user, name='logout_user'),   
    path('create_post/', create_post, name='create_post'),
    path('category_post/', category_post, name='category_post'),
    path('product_list/<slug:category_slug>/', product_list, name='product_list_category'),
    path('product_detail/<int:id>/', product_detail, name='product_detail'),
    # path('category/<int>/', category_list, name='category'),
    path('category/<category>/', CategoryListView.as_view(), name='category'),
    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    
    
