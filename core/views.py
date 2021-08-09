from rest_framework.decorators import api_view
from rest_framework.response import Response

from .services import *
from .exceptions import InvalidMissingFile

# Create your views here.
@api_view(['POST'])
def fill_order_database(request):
    try:
        fill_database(request.FILES['file'])
    except:
        raise InvalidMissingFile

    return Response()

@api_view(['GET'])
def all_orders(request):
    return Response(get_all_orders())