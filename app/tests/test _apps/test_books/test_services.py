from unittest.mock import patch
from requests import Response

from src.books.services import fetch_from_google_books, get_formatted_publication_date


def test_fetch_from_google_books_empty_query():
    result1 = fetch_from_google_books(query="")
    result2 = fetch_from_google_books(query="   ")
    result3 = fetch_from_google_books(query=" ")

    assert result1 == []
    assert result2 == []
    assert result3 == []


@patch("requests.get")
def test_fetch_from_google_books_error_response(mock_requests_get):
    mock_requests_get.return_value = Response()
    mock_requests_get.return_value.status_code = 400

    result = fetch_from_google_books(query="some query")

    assert result == []


def test_get_formatted_publication_date():
    formatted_date = get_formatted_publication_date("2021")

    assert formatted_date == "2021-01-01"
