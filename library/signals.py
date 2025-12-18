from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Book

@receiver(post_save, sender=Book)
def notify_new_book(sender, instance, created, **kwargs):
    if created:
        print("New book added:", instance.title)
