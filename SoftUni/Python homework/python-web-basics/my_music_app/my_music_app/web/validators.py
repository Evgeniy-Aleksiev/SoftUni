import re

from django.core.exceptions import ValidationError


def validate_letters_numbers_underscore(username):
    if not re.match(r'[a-zA-Z_]\w+', username):
        raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")
