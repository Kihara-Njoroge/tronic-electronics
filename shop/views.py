from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator

# Create your views here.


def home(request):
    products = Product.objects.all()
    paginator = Paginator(products, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}
    return render(request, 'home.html', context)


def vendors(request):
    context = {}
    return render(request, 'vendors.html', context)


def contactPage(request):
    context = {}
    return render(request, 'contact-form.html', context)


def cartPage(request):
    context = {}
    return render(request, 'cart.html', context)


def checkout(request):
    context = {}
    return render(request, 'checkout.html', context)


def loginPage(request):
    context = {}
    return render(request, 'login.html', context)


def registerPage(request):
    context = {}
    return render(request, 'register-form.html', context)


def terms(request):
    context = {}
    return render(request, 'terms-conditions.html', context)


def privacy(request):
    context = {}
    return render(request, 'privacy.html', context)


def faq(request):
    context = {}
    return render(request, 'faq.html', context)
