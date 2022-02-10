from rest_framework.decorators import api_view
from rest_framework.response import Response
from store.models import Customer, Product, Order, OrderItem
from . serializers import ProductSerializer, OrderItemSerializer, OrderSerializer
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import CustomerSerializer
from django.contrib.auth.hashers import make_password, check_password

@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/products',
        'GET /api/product/:id',
    ]
    return Response(routes)

#------------ Product -----------------
@api_view(['GET'])
def getProducts(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getProduct(request, pk):
    product = Product.objects.get(id = pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getProductByCategory(request, pk):
    product = Product.objects.get(category = pk)
    if product:
         serializer = ProductSerializer(product)
         if serializer is not None:
            return Response(serializer.data, status=status.HTTP_201_CREATED)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_500.DoesNotExist)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def postProduct(request):
    product_data = JSONParser().parse(request)
    serializer = ProductSerializer(data = product_data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateProduct(request, pk):
    product_data = JSONParser().parse(request)
    product = Product.objects.get(id = pk)
    serializer = ProductSerializer(product, data = product_data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#------------ Order -----------------
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getOrder(request):
    order = Order.objects.all()
    serializer = OrderSerializer(order, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getOrderByCustomer(request , pk):
    order_data = Order.objects.get(customer_id = pk)
    print(order_data.complete)
    if order_data:
        serializer = OrderSerializer(order_data, many=False)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def makeOrder(request, pk):
    order_data = JSONParser().parse(request)
    customer =  Customer.objects.get(id = pk)
    print(customer.name)
    serializer = OrderSerializer(customer, data = order_data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateOrderItem(request, pk):
    order_item_data = JSONParser().parse(request)
    order_item = OrderItem.objects.get(id = pk)
    serializer = OrderItemSerializer(order_item, data = order_item_data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ------------------- Customer --------------------------
def validateCustomerForm(cust):
    error = None
    if not cust.name:
        error = "name is required"
    elif not cust.phone:
        error = "phone is required"
    elif not cust.email:
        error = "email is required"
    elif cust.isEmailExist():
        error = "This Email ID is already registered"
    elif not cust.password:
        error = "password is required"
    elif len(cust.password) < 8:
        error = "password must be greater or equal than 8 char."
    return error

@api_view(['POST'])
def signup(request):
    if request.method == 'POST':
        name = request.data['name']
        phone = request.data['phone']
        email = request.data['email']
        password = request.data['password']
        form_data =  {
            "name":name,
                "phone":phone,
                "email":email,
        }
        cust = Customer(
                name = name,
                phone = phone,
                email = email,
                password = password
            )
        error = validateCustomerForm(cust)
        if not error:
            request.data['password'] = make_password(request.data['password'])
            customerSerializers = CustomerSerializer(data=request.data)
            if customerSerializers.is_valid():
                customerSerializers.save()
                return Response(customerSerializers.data)
            else:
                return Response(customerSerializers.errors)
        else:
            return Response({"message": "something went wrong"})

@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        loginEmail = request.data.get('email')
        loginPassword = request.data.get('password')
        cust = None
        is_successfull = None
        try:
            cust = Customer.objects.get(email = loginEmail)
        except:
            return Response({"message":"USER DOES NOT EXIST"})
        if cust:
            is_successfull = check_password(loginPassword, cust.password)
        if is_successfull:
            return Response({"name" : cust.name, "phone": cust.phone, "email": cust.email, "password": cust.password, "id": cust.id})
        else:
            return Response({"message" : "username and password doesn't exist"})
