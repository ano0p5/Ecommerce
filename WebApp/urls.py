from django.urls import path
from WebApp import views

urlpatterns=[
    path('',views.homepage,name="home"),
    path('about/',views.aboutpage,name="about"),
    path('contact/',views.contactpage,name="contact"),
    path('shop/',views.shoppage,name="shop"),
    path('news/',views.news_page,name="news"),
    path('save_contact/',views.save_contact,name="save_contact"),
    path('singleproduct/<int:pid>/',views.single_product,name="singleproduct"),
    path('single_category/<cat_name>/',views.single_category,name="single_category"),
    path('user_login/',views.user_login,name="user_login"),
    path('save_register/',views.save_register,name="save_register"),
    path('loginbycheck/',views.loginbycheck,name="loginbycheck"),
    path('user_logout/',views.user_logout,name="user_logout"),
    path('save_cart/',views.save_cart,name="save_cart"),
    path('cartpage/',views.cartpage,name="cartpage"),
    path('delete_cart/<int:cid>/',views.delete_cart,name="delete_cart"),
    path('user_register/',views.user_register,name="user_register"),
    path('checkout_page/',views.checkout_page,name="checkout_page"),
    path('payment/',views.payment,name="payment"),
    path('save_check/',views.save_check,name="save_check"),
]


