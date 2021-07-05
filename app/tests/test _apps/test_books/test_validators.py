import pytest
from django.core.exceptions import ValidationError

from src.books.validators import isbn_validator


def test_isbn_validator_invalid_length():
    with pytest.raises(ValidationError):
        isbn_validator("420")

    with pytest.raises(ValidationError):
        isbn_validator("1234567890987654321")


def test_isbn_validator_invalid_checksum():
    with pytest.raises(ValidationError):
        isbn_validator("1492020665")

    with pytest.raises(ValidationError):
        isbn_validator("9781492020661")


def test_isbn_validator_valid_isbn():
    valid_isbn10 = "1492020664"
    valid_isbn13 = "9781492020660"

    result_isbn10 = isbn_validator(valid_isbn10)
    result_isbn13 = isbn_validator(valid_isbn13)

    assert valid_isbn10 == result_isbn10
    assert valid_isbn13 == result_isbn13


