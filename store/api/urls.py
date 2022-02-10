from xml.etree.ElementInclude import include
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.getRoutes),
    # Product 
    path('products/', views.getProducts),
    path('products/product/<str:pk>', views.getProduct),
    path('products/category/<str:pk>', views.getProductByCategory),
    path('products/add', views.postProduct),
    path('product/update/<str:pk>', views.updateProduct),
    
    # Order 
    path('products/get/all/order', views.getOrder),
    path('products/order/<str:pk>', views.getOrderByCustomer),
    path('products/add/order/<str:pk>', views.makeOrder),

    # Customer
    path('signup/', views.signup),
    path('login/', views.login),
]

