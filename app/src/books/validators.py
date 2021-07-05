import re

from django.core.exceptions import ValidationError


def isbn_validator(subject: str) -> str:
    pattern = r"^(?=(?:\D*\d){10}(?:(?:\D*\d){3})?$)[\d-]+$"
    if re.match(pattern, subject):
        digits = subject.replace("-", "")
        digits = list(map(int, list(digits)))

        last_digit = digits.pop()

        if len(digits) == 9:
            checksum = 0
            for position, digit in enumerate(digits):
                checksum += (position + 1) * digit
            check = checksum % 11
            if check == 10:
                check = "X"
        elif len(digits) == 12:
            checksum = 0
            for position, digit in enumerate(digits):
                if (position + 1) % 2 == 0:
                    checksum += 3 * digit
                else:
                    checksum += digit
            check = (10 - (checksum % 10)) % 10

        if str(check) == str(last_digit):
            return subject

    raise ValidationError("Invalid ISBN number")
