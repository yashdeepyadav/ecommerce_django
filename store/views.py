from unicodedata import category
from django.shortcuts import render
from . models import *

# Create your views here.

def store(request):
  products = Product.objects.all()
  categories = Category.objects.all()
  context={'products':products , 'categories': categories}
  return render(request, 'store/store.html',context)


def cart(request):
  # if request.user.is_authenticated:
  #   customer= request.user.customer
  #   order ,created = Order.objects.get_or_create(customer=customer,complete=False)
  #   items = order.orderitem_set.all()
  # else:
  #   items=[]
  # context={'items':items}
  return render(request,'store/cart.html')


def checkout(request):
  context={}
  return render(request,'store/checkout.html',context)

def signup(request):
  # context={}
  return render(request,'store/signup.html')

def login(request):
  # context={}
  return render(request,'store/login.html')


