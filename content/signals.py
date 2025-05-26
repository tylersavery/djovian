from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from content.models import Example


@receiver(post_save, sender=Example)
def post_save_example(sender, instance: Example, created, **kwargs):

    if created:
        print(f"New Example Created ({instance.title})")


@receiver(pre_save, sender=Example)
def pre_save_contribution(sender, instance: Example, *args, **kwargs):
    print(f"About to save Example ({instance.title})")
