from django.conf import settings


def pytest_configure():
    settings.GOOGLE_API_KEY = "mockKey"
