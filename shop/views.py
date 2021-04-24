from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.core.paginator import Paginator
from django.urls import reverse
from django.views.generic import TemplateView
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login, logout
import json
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import stripe
import datetime
from .models import *
from .forms import *
from .utils import cookieCart, cartData, guestOrder
from .filters import ProductFilter


def home(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    products = Product.objects.all()
    myFilter = ProductFilter(request.GET, queryset=products)
    products = myFilter.qs

    paginator = Paginator(products, 9)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    context = {'products': products,
               'cartItems': cartItems, 'page_obj': page_obj, 'myFilter': myFilter}
    return render(request, 'home.html', context)


def cartPage(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'cart.html', context)


def CheckoutPage(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    if request.user.is_authenticated:
        checkout_total = order.get_cart_total
    else:
        checkout_total = order['get_cart_total']

    context = {"data": data, "order": order, "items": items,
               "cartItems": cartItems, "checkout_total": checkout_total, }
    return render(request, 'checkout.html', context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(
        customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(
        order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)


def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
    else:
        customer, order = guestOrder(request, data)

    total = float(data['form']['total'])
    order.transaction_id = transaction_id

    if total == order.get_cart_total:
        order.complete = True
    order.save()

    if order.shipping == True:
        ShippingAdress.objects.create(
            customer=customer,
            order=order,
            town=data['shipping']['town'],
            street=data['shipping']['street'],
            estate=data['shipping']['estate'],
            address=data['shipping']['address'],
        )

    return JsonResponse('Payment submitted..', safe=False)


def vendors(request):
    data = cartData(request)
    cartItems = data['cartItems']

    vendors = Vendor.objects.all()
    paginator = Paginator(vendors, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj, 'cartItems': cartItems}
    return render(request, 'vendors.html', context)


def contactPage(request):
    data = cartData(request)
    cartItems = data['cartItems']
    context = {'cartItems': cartItems}
    return render(request, 'contact-form.html', context)


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'username or password incorrect')

    data = cartData(request)
    cartItems = data['cartItems']
    context = {'cartItems': cartItems}
    return render(request, 'login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def registerPage(request):
    data = cartData(request)
    cartItems = data['cartItems']

    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            messages.success(
                request, 'Account created successfully for ' + username)

            return redirect('login')

    context = {'cartItems': cartItems, 'form': form}

    return render(request, 'register-form.html', context)


def productDetail(request, pk):
    data = cartData(request)
    cartItems = data['cartItems']
    context = {'cartItems': cartItems}
    product = Product.objects.get(id=pk)
    products = Product.objects.all()
    products_category = products.filter(category=product.category)

    context = {'product': product,
               'cartItems': cartItems, 'products_category': products_category}
    return render(request, 'product_detail.html', context)


def terms(request):
    data = cartData(request)
    cartItems = data['cartItems']
    context = {'cartItems': cartItems}
    return render(request, 'terms-conditions.html', context)


def privacy(request):
    data = cartData(request)
    cartItems = data['cartItems']
    context = {'cartItems': cartItems}
    return render(request, 'privacy.html', context)


def faq(request):
    data = cartData(request)
    cartItems = data['cartItems']
    context = {'cartItems': cartItems}
    return render(request, 'faq.html', context)
