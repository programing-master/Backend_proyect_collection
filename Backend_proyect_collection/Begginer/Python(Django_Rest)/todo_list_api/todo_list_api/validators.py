from rest_framework.validators import ValidationError;

def validate_data(value):
     valid_options=['high','low','medium'];
     if value.lower() not in valid_options:
         raise ValidationError(f'Value: {value} is not valid')