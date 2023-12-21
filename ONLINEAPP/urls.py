from django.urls import path
from ONLINEAPP import views
from.models import*

urlpatterns = [
  
    path('shopping',views.shopping,name='shopping'),
    path('shop',views.shop,name='shop'),
    path('cart',views.cart,name='cart'),
    path('view_cart',views.view_cart,name='view_cart'),
    path('about',views.about,name='about'),
    path('single_product/<int:product_id>',views.single_product,name='single_product'),
    path('login',views.login,name='login'),
    path('signup',views.signup,name='signup'),
    path('filtered_products/<str:category>',views.filtered_products,name='filtered_products'),
    path('delete_product3/<int:product_id>',views.delete_product3,name='delete_product3')
    


    
]
