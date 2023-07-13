from django.urls import path
from . import views



urlpatterns = [
    # path('cust_menu/', views.cust_menu, name='cust_menu'),
    path('mem_reg/', views.mem_reg, name='mem_reg'),
    path('display_all/', views.display_all, name='display_all'),
    # path('internal_account/', views.internal_account, name='internal_account'),
    path('member_detail/<int:id>/', views.member_detail, name='member_detail'),
    path('delete_object/<int:id>/', views.delete_object, name='delete_object'),
    path('comment/<int:id>/', views.comment, name='comment'),
    path('display_comment/', views.display_comment, name='display_comment'),
    # path('modify_delete/', views.modify_delete, name='modify_delete'),
    # path('list_customer/', views.list_customer, name='list_customer'),
    # path('update_customer/<str:custom_id>/', views.update_customer, name='update_customer'),
    # path('delete_customer/<str:custom_id>/', views.delete_customer, name='delete_customer'),
    
]