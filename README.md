
# About this project
This applications is your virtual library that allows you to store information about books you're interested in. It covers basic CRUD functionality. It was created using Django framework.

Books can be listed and filtered based on following properties:
* title
* author
* publication date
* language

![image](https://user-images.githubusercontent.com/48218942/124509237-e08a5e80-ddd1-11eb-8530-d5b5e698d61a.png)

Books can be added either manually through form or imported via Google Books API. Books are fetched from API according to keywords provided by user and presented as list of selectable elements. User can choose which ones are to be saved.

## Rest API
Applicaton also provides REST Api, which consists of 1 endpoint:
* `GET - /api/books`

This endpoint returns list of all stored books in JSON format. It supports filtering through following query paremeters:
* `title`
* `author`
* `language`
* `publication_date__gt`
* `publication_date__lt`

Example response:
```
[
  {
    "id": 1,
    "title": "The Lord of the Rings",
    "author": "J. R. R. Tolkien",
    "publicationDate": "2012-01-01",
    "pageCount": 1178,
    "coverUrl": "http://books.google.com/books/content?id=...,
    "language": "en",
    "isbn": "0544003411"
  },
  {
    "id": 2,
    "title": "Dune",
    "author": "Frank Herbert",
    "publicationDate": "2003-08-26",
    "pageCount": 897,
    "coverUrl": "http://books.google.com/books/content?id=...",
    "language": "en",
    "isbn": "9781101658055"
  }
]
```
