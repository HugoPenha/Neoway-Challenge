from django.db import models

# Create your models here.
class Order(models.Model):
    cpf = models.CharField(max_length=20, null=False)
    private = models.BooleanField()
    incomplete = models.BooleanField()
    last_purchase_date = models.DateField(blank=True, null=True)
    average_ticket = models.FloatField(null=True)
    last_purchase_ticket = models.FloatField(null=True)
    frequent_store = models.CharField(max_length=20, null=True, blank=True)
    last_purchase_store = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.cpf

    