from django.urls import path
from adminapp import views
from.models import*

urlpatterns = [
    path('',views.admin,name='admin'),
    path('add_category',views.add_category,name='add_category'),
    path('add_product',views.add_product,name='add_product'),
    path('view_product',views.view_product,name='view_product'),
    path('edit_product',views.edit_product,name='edit_product'),
    path('edit_changes/<int:id>',views.edit_changes,name='edit_changes'),
    path('update/<int:id>',views.update,name='update'),
    path('delete_product',views.delete_product,name='delete_product'),
    path('delete_product2/<int:id>',views.delete_product2,name='delete_product2'),
    path('user_details',views.user_details,name='user_details'),
    path('view_complaints',views.view_complaints,name='view_complaints'),
    path('contact',views.contact,name='contact'),
    path('checkout',views.checkout,name='checkout'),
    path('view_checkout',views.view_checkout,name='view_checkout'),
    path('order',views.order,name='order')




]