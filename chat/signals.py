from django.dispatch import receiver
from django.db.models.signals import post_save , pre_save
from django.contrib.auth.models import User
from .models import  Threads
from django.utils.text import slugify
from uuid import uuid4 







@receiver( pre_save , sender=Threads)
def slugFieldCreationSignal(sender, instance, *args, **kwargs):
    # slug = slugify(instance.name)
    slug = uuid4()
    instance.slug = slug 