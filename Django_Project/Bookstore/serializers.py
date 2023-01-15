import datetime
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Book, Order, Author, Client, Genre, Section


class BookSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.SlugRelatedField(queryset=Author.objects.all(), slug_field='last_name')
    genre_genre = serializers.SlugRelatedField(queryset=Genre.objects.all(), slug_field='genre')

    class Meta:
        model = Book
        fields = ['url', 'book_id', 'title', 'author', 'price', 'publisher', 'genre_genre', 'number_of_copies', 'year_of_publication']


class TitlePriceField(serializers.SlugRelatedField):
    def to_representation(self, obj):
        return f"{obj.title} price: {obj.price}"

    def to_internal_value(self, data):
        title = data.split("price:")[0].strip()
        obj = self.get_queryset().filter(title=title).first()
        if obj is None:
            raise serializers.ValidationError("Invalid title")
        return obj


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    book_info = TitlePriceField(queryset=Book.objects.all(), slug_field='title')
    purchase_date = serializers.DateField(default=datetime.datetime.now(), read_only=True)
    owner = serializers.ReadOnlyField(source='owner.username')

    def create(self, validated_data):
        validated_data['purchase_date'] = datetime.datetime.now().date()
        return super().create(validated_data)

    class Meta:
        model = Order
        fields = ['url', 'order_id', 'purchase_date', 'owner', 'book_info']


class UserOrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ['url', 'order_id', 'book_book', 'purchase_date', 'price','owner']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    orders = UserOrderSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = ['url', 'pk', 'username', 'book']


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    authors = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='authorDetail')

    class Meta:
        model = Author
        fields = ['url', 'author_id', 'name', 'last_name', 'authors']


class ClientSerializer(serializers.HyperlinkedModelSerializer):
    orders = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='orderDetail')
    class Meta:
        model = Client
        fields = ['url', 'client_id', 'name', 'last_name', 'birth_date', 'city', 'address', 'orders']


class GenreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Genre
        fields = ['url', 'genre_id', 'genre']


# class SectionSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Section
#         fields = ['section_id', 'section_name']