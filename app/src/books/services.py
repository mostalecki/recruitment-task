import json
from typing import List, Dict

import requests
from django.conf import settings

from src.books.models import Book

GOOGLE_BOOKS_API_BASE_URL = "https://www.googleapis.com/books/v1/volumes"


def fetch_from_google_books(*, query: str) -> List[Book]:
    if not query.strip():
        return []

    query_url = google_books_api_query_url_builder(query=query)
    response = requests.get(query_url)

    if response.status_code != 200:
        return []

    books_dict = google_books_response_parser(json.loads(response.text))

    return books_dict


def google_books_api_query_url_builder(*, query: str) -> str:
    return f"{GOOGLE_BOOKS_API_BASE_URL}?q={query}&key={settings.GOOGLE_API_KEY}"


def google_books_response_parser(response: Dict) -> List[Dict]:
    return [
        {
            "volume_id": item["id"],
            "title": item["volumeInfo"]["title"],
            "author": ", ".join(item["volumeInfo"]["authors"]),
            "publication_date": get_formatted_publication_date(
                item["volumeInfo"]["publishedDate"]
            ),
            "page_count": item.get("volumeInfo").get("pageCount", None),
            "cover_url": item["volumeInfo"]["imageLinks"]["thumbnail"]
            if "imageLinks" in item["volumeInfo"]
            else None,
            "language": item["volumeInfo"]["language"],
            "isbn": item["volumeInfo"]["industryIdentifiers"][0]["identifier"]
            if "industryIdentifiers" in item["volumeInfo"]
            else None,
        }
        for item in response["items"]
    ]


def books_bulk_create_from_dict(books_dict: Dict) -> List[Book]:
    return [Book(**book) for book in books_dict]


def get_formatted_publication_date(date: str) -> str:
    """Handles publication dates with year only"""
    if len(date) == 4:
        return f"{date}-01-01"
    return date
