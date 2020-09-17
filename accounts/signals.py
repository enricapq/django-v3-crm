""" Signals https://docs.djangoproject.com/en/3.0/topics/signals/
"""
from django.db.models.signals import post_save
from django.contrib.auth.models import Group, User
from .models import Customer


def customer_profile(sender, instance, created, **kwargs):
    """
    signal call the function. Update apps.py and installed_app
    """
    if created:
        # automatically when a user register create the customer
        group = Group.objects.get(name='customer')
        instance.groups.add(group)

        # create customer when user is registered
        Customer.objects.create(
            user=instance,
            name=instance.username
        )
        print('profile created')


post_save.connect(customer_profile, sender=User)
