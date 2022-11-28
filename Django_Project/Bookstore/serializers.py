from rest_framework import serializers
from .models import Book, Order, Author, Client, Genre


class BookSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.SlugRelatedField(queryset=Author.objects.all(), slug_field='last_name')
    genre_genre = serializers.SlugRelatedField(queryset=Genre.objects.all(), slug_field='genre')

    class Meta:
        model = Book
        fields = ['book_id', 'title', 'author', 'price', 'publisher', 'genre_genre', 'number_of_copies', 'year_of_publication']


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    book_book = serializers.SlugRelatedField(queryset=Book.objects.all(), slug_field='title')
    client_client = serializers.SlugRelatedField(queryset=Client.objects.all(), slug_field='name')

    class Meta:
        model = Order
        fields = ['order_id', 'book_book', 'client_client', 'purchase_date', 'price']


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    books = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='book-detail')

    class Meta:
        model = Author
        fields = ['author_id', 'name', 'last_name', 'books']


class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = ['client_id', 'name', 'last_name', 'birth_date', 'city', 'address']

class GenreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Genre
        fields = ['genre_id', 'genre']
