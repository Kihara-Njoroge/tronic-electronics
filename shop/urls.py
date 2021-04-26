from django.urls import path
from shop.views import(
    CheckoutPage, home,
    cartPage, vendors, loginPage,
    contactPage, registerPage, VendorRegisterPage,
    terms, privacy, faq, updateItem, processOrder,
    productDetail, logoutUser, accountSettings,
)

urlpatterns = [
    path('', home, name='home'),
    path('tronic-vendors/', vendors, name='vendors'),
    path('contact-us/', contactPage, name='contact'),
    path('cart/', cartPage, name='cart'),
    path('checkout/', CheckoutPage, name='checkout'),
    path('update_item/', updateItem, name='update_item'),
    path('process_order/', processOrder, name='process_order'),
    path('login/', loginPage, name='login'),
    path('logout/', logoutUser, name='logout'),
    path('register/', registerPage, name='register'),
    path('vendor_registration/', VendorRegisterPage, name='vendor_registration'),
    path('product_detail/<str:pk>/', productDetail, name='product_detail'),
    path('settings/', accountSettings, name='settings'),

    path('terms&conditions/', terms, name='termsandconditions'),
    path('privacy-policy/', privacy, name='privacy-policy'),
    path('tronic-faq/',  faq, name='faq'),
]
