from django.conf.urls import url, include
from django.urls import path
from .views import *


urlpatterns = [
    path('fill/order/', fill_order_database),
    path('all-orders/', all_orders),
]