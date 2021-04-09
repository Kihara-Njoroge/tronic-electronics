from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tronic-vendors/', views.vendors, name='vendors'),
    path('contact-us/', views.contactPage, name='contact'),
    path('cart/', views.cartPage, name='cart'),
    path('login/', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'),
    path('checkout/', views.checkout, name='checkout'),



    path('terms&conditions/', views.terms, name='termsandconditions'),
    path('privacy-policy/', views.privacy, name='privacy-policy'),
    path('tronic-faq/',  views.faq, name='faq'),
]
