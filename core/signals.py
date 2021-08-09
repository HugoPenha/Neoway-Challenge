from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import *

@receiver(post_save, sender=Order)
def add_job_coordinates(sender, instance=None, created=False, **kwargs):
    if created:
        if instance.cpf is not None:
            cpf = instance.cpf.replace('.', '')
            cpf = cpf.replace('-', '')
            instance.cpf = cpf

        if instance.frequent_store is not None:
            frequent_store = instance.frequent_store.replace('.', '')
            frequent_store = frequent_store.replace('/', '')
            frequent_store = frequent_store.replace('-', '')
            instance.frequent_store = frequent_store

        if instance.last_purchase_store is not None:
            last_purchase_store = instance.last_purchase_store.replace('.', '')
            last_purchase_store = last_purchase_store.replace('/', '')
            last_purchase_store = last_purchase_store.replace('-', '')
            instance.last_purchase_store = last_purchase_store

        instance.save()

        