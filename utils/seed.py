import json
from django.db import transaction
from toscrape_app.models import Author, Quote


def load_data_from_json(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)


def get_or_create_author(author_data):
    author, created = Author.objects.get_or_create(
        fullname=author_data['fullname'],
        defaults={
            'born_date': author_data['born_date'],
            'born_location': author_data['born_location'],
            'description': author_data['description']
        }
    )
    return author


def create_quote(quote_data, author):
    quote = Quote(
        quote=quote_data['quote'],
        author=author,
        tags=quote_data['tags']
    )
    quote.save()


authors_data = load_data_from_json('utils/authors.json')

quotes_data = load_data_from_json('utils/quotes.json')

with transaction.atomic():
    for author_data in authors_data:
        get_or_create_author(author_data)

    for quote_data in quotes_data:
        author = Author.objects.get(fullname=quote_data['author'])
        create_quote(quote_data, author)