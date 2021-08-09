import json

from pycpfcnpj import cpfcnpj #Python module to deal with brazilian register numbers (CPF and CNPJ)

from .models import Order
from .serializers import *

def convert_to_none(value):
    if value == 'NULL':
        return None
    return value

def convert_to_bool(value):
    if value == '1':
        return True
    return False

#Insert database
def register_valid_registered_numbers(line):
    line_dict = {
        'cpf' : line[0],
        'private' : convert_to_bool(line[1]),
        'incomplete' : convert_to_bool(line[2]),
        'last_purchase_date' : convert_to_none(line[3]),
        'average_ticket' : convert_to_none(line[4].replace(',', '.')),
        'last_purchase_ticket' : convert_to_none(line[5].replace(',', '.')),
        'frequent_store' : convert_to_none(line[6]),
        'last_purchase_store' : convert_to_none(line[7])
    }
    Order.objects.create(**line_dict)

#Function to recieve data and fill the Order table 
def fill_database(request_file):
    #Default value for split
    split_char = None
    #Treatment for if it is a comma-separated CSV file
    if str(request_file).endswith(".csv"):
        split_char = ','

    for line in request_file:
        formatted_line = line.decode()
        formatted_line = formatted_line.split(split_char)
        
        #Register only those with a valid number
        if cpfcnpj.validate(formatted_line[0]):
            register_valid_registered_numbers(formatted_line)
    return True

def get_all_orders():
    return OrderSerializer(Order.objects.all()[:100], many=True).data