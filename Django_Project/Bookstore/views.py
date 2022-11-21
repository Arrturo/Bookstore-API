from django.shortcuts import render
from rest_framework import generics
from .models import Book, Order, Author, Client
from .serializers import *
# Create your views here.

class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    name = 'Books'
    serializer_class = BookSerializer

class AuthorList(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    name = 'Authors'
    serializer_class = AuthorSerializer

class GenreList(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    name = 'Genres'
    serializer_class = GenreSerializer

class ClientList(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    name = 'Clients'
    serializer_class = ClientSerializer

class OrdersList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    name = 'Orders'
    serializer_class = OrderSerializer
