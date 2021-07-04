from django.core.exceptions import ValidationError


def isbn_validator(subject: str) -> str:
    if len(subject) not in [10, 13]:
        raise ValidationError("Invalid ISBN number")

    return subject
