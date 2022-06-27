from django.core.exceptions import ValidationError
# from event.models import *




def validate_phone(value):
    if value.startswith(('077','078','075')) and len(value) == 11:
        return value
    else:
        raise ValidationError('Not a Phone Format')