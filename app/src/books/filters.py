import django_filters

from src.books.enums import Language


class BookFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr="iexact")
    author = django_filters.CharFilter(lookup_expr="iexact")
    language = django_filters.ChoiceFilter(choices=Language.choices)
    publication_date__gt = django_filters.DateFilter(field_name='publication_date', lookup_expr='gt')
    publication_date__lt = django_filters.NumberFilter(field_name='publication_date', lookup_expr='lt')
