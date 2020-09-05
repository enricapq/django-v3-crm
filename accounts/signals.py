""" Signals https://docs.djangoproject.com/en/3.0/topics/signals/
"""
import logging

from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.auth.models import User
from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """
    signal call the function
    """
    # if created:
    #     Profile.objects.create(user=instance)
    #     logging.info('Profile created!')

    # workaround for "User has no profile" error
    Profile.objects.get_or_create(user=instance)
    logging.info('Profile get or created!')
    print('Profile get or created!')

# connect the receiver, create_profile, to the sender, User, that triggered it
# comment and use @receiver
#post_save.connect(create_profile, sender=User)

@receiver(post_save, sender=User)
def update_profile(sender, instance, created, **kwargs):
    if created == False:
        instance.profile.save()
        logging.info('Profile updated!')
        print('Profile updated!')

# comment and use @receiver
#post_save.connect(update_profile, sender=User)
