from django.db.models.signals import post_save
from django.contrib.auth.models import User#sender
from django.dispatch import receiver#receiver
from .models import Profile, Payment, Address

@receiver(post_save, sender = User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender = User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
    
@receiver(post_save, sender = User)
def create_payment(sender, instance, created, **kwargs):
    if created:
        Payment.objects.create(user=instance)

@receiver(post_save, sender = User)
def save_payment(sender, instance, **kwargs):
    instance.address.save()

@receiver(post_save, sender = User)
def create_address(sender, instance, created, **kwargs):
    if created:
        Address.objects.create(user=instance)

@receiver(post_save, sender = User)
def save_address(sender, instance, **kwargs):
    instance.address.save()
    