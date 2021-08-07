from rest_framework.exceptions import APIException
from django.utils.translation import ugettext as _


class InvalidMissingFile(APIException):
    status_code = 404
    default_detail = _('Arquivo inválido ou não encontrado')
    default_code = 'permission_denied'