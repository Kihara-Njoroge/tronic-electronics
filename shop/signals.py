from django.db.models.signals import post_save
from django.contrib.auth.models import User, Group
from .models import Customer, Vendor


def customer_profile(sender, instance, created, ** kwargs):
    if created:
        group = Group.objects.get(name='customer')
        instance.groups.add(group)
        Customer.objects.create(user=instance, name=instance.username)

        print('Cusromer profile Created')


post_save.connect(customer_profile, sender=User)


def vendor_profile(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='vendor')
        instance.groups.add(group)
        Vendor.objects.create(first_name=instance.first_name,
                              second_name=instance.last_name, email=instance.email),

        print('Vendors profile created')


post_save.connect(vendor_profile, sender=User)
