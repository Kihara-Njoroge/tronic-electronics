from django.urls import path
from shop.views import(
    CheckoutPage, home,
    cartPage, loginPage,
    contactPage, registerPage,
    terms, privacy, faq, updateItem, processOrder,
    productDetail, logoutUser,
)

urlpatterns = [
    path('', home, name='home'),
    path('contact-us/', contactPage, name='contact'),
    path('cart/', cartPage, name='cart'),
    path('checkout/', CheckoutPage, name='checkout'),
    path('update_item/', updateItem, name='update_item'),
    path('process_order/', processOrder, name='process_order'),
    path('login/', loginPage, name='login'),
    path('logout/', logoutUser, name='logout'),
    path('register/', registerPage, name='register'),
    path('product_detail/<str:pk>/', productDetail, name='product_detail'),
    path('terms&conditions/', terms, name='termsandconditions'),
    path('privacy-policy/', privacy, name='privacy-policy'),
    path('tronic-faq/',  faq, name='faq'),
]
