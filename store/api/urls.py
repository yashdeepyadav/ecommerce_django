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

    # Order Item
    path('products/get/all/order-items', views.getOrderItem),
    path('products/order-items/<str:pk>', views.getOrderItemByCustomer),
    path('products/add/order-item', views.makeOrderItem),

     # Category
    path('products/get/all/category', views.getCategory),    
    path('products/category/get/<str:pk>', views.getCategoryById),
    path('products/category/add/', views.addCategory),
    path('products/category/update-one/<str:pk>', views.updateCategory),
    path('products/category/delete/<str:pk>', views.deleteCategoryById),

    # Customer
    path('signup/', views.signup),
    path('login/', views.login),
]

