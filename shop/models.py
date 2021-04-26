from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=150, blank=False, null=False)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.name


class Vendor(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=100, null=False, blank=False)
    second_name = models.CharField(
        max_length=100, null=False, blank=False)
    phone = PhoneNumberField(null=True, blank=True, unique=True)
    email = models.EmailField(max_length=254)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return (self.first_name + " " + self.second_name)

    @property
    def potrtaitURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Product(models.Model):
    category_choices = (
        ('Computing', 'Computing'),
        ('Gaming', 'Gaming'),
        ('Phones', 'Phones'),
        ('TV & Vidoe', 'TV & Video'),
        ('Photography', 'Photography'),
        ('Music & Sound', 'Music & Sound'),
        ('Home Applliances', 'Home Applliances'),
        ('Office Electronics', 'Office Electronics')
    )
    name = models.CharField(max_length=100, null=False, blank=False)
    price = models.DecimalField(decimal_places=2, max_digits=7)
    description = models.CharField(max_length=150, null=True, blank=True)
    category = models.CharField(
        max_length=150, choices=category_choices, default='Computing')
    vendor = models.ForeignKey(
        Vendor, on_delete=models.SET_NULL, null=True, blank=True,)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    @property
    def vendorName(self):
        if self.vendor == None:
            vendor = 'Tronic Electronics'
            return vendor
        else:
            return self.vendor


class Order(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_created=True, null=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=254, null=True)
    shipping = models.BooleanField(default=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.product)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total


class ShippingAdress(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    town = models.CharField(max_length=254, null=False)
    street = models.CharField(max_length=254, null=False)
    estate = models.CharField(max_length=254, null=False)
    address = models.CharField(max_length=254, null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
