from django.urls import path , include
from . import views

urlpatterns = [
    path('', views.store,name="store"),
    path('cart/', views.cart,name="cart"),
    path('checkout/', views.checkout,name="checkout"),
    path('api/', include('store.api.urls')),
 
    # customer
    # path('', include('djoser.urls')),
    # path('', include('djoser.urls.authtoken')),
    path('signup/', views.signup , name="signup"),
    path('login/', views.login, name="login"),
]
