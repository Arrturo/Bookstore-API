from django.shortcuts import render
from rest_framework import generics
from .models import Book, Order, Author, Client
from django.http import Http404
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import authentication, permissions
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS
from rest_framework.reverse import reverse
from django.core.paginator import Paginator
from django_filters import AllValuesFilter, DateTimeFilter, NumberFilter, FilterSet


# Create your views here.


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class BookList(APIView):
    permission_classes = [IsAdminUser | ReadOnly]
    name = 'Books'
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_object(self, pk):
        try:
            return Book.objects.get(id=pk)
        except Book.DoesNotExist:
            raise Http404

    def get(self, request, Format=None):
        Books = Book.objects.all()
        Serializer = BookSerializer(Books, many=True)
        return Response(Serializer.data)
    def post(self, request, Format=None):
        Serializer = BookSerializer(data=request.data)
        if Serializer.is_valid():
            Serializer.save()
            return Response(Serializer.data, status=status.HTTP_201_CREATED)
        return Response(Serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    name = 'book-detail'



class AuthorList(APIView):
    permission_classes = [IsAdminUser | ReadOnly]
    name = 'Authors'
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    pagination = Paginator(queryset, 5)

    def get_object(self, pk):
        try:
            return Author.objects.get(pk=pk)
        except Author.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        Authors = Author.objects.all()
        Serializer = AuthorSerializer(Authors, many=True)
        return Response(Serializer.data)

    def post(self, request, format=None):
        Serializer = AuthorSerializer(data=request.data)
        if Serializer.is_valid():
            Serializer.save()
            return Response(Serializer.data, status=status.HTTP_201_CREATED)
        return Response(Serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    name = 'Author-detail'


class GenreList(APIView):
    permission_classes = [IsAdminUser | ReadOnly]
    name = 'Genres'
    queryset = Genre.objects.all
    serializer_class = GenreSerializer

    def get_object(self, pk):
            try:
                return Genre.objects.get(pk=pk)
            except Genre.DoesNotExist:
                raise Http404

    def get(self, request, format=None):
            Genres = Genre.objects.all()
            Serializer = GenreSerializer(Genres, many=True)
            return Response(Serializer.data)

    def post(self, request, format=None):
            Serializers = GenreSerializer(data=request.data)
            if Serializers.is_valid():
                Serializers.save()
                return Response(Serializers.data, status=status.HTTP_201_CREATED)
            return Response(Serializers.errors, status=status.HTTP_400_BAD_REQUEST)



class GenreDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    name = 'Genre-detail'

class ClientList(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser | ReadOnly]
    name = 'Clients'
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    def get_object(self, pk):
            try:
                return Client.objects.get(pk=pk)
            except Client.DoesNotExist:
                raise Http404

    def get(self, request, format=None):
            Clients = Client.objects.all()
            Serializer = ClientSerializer(Clients, many=True)
            return Response(Serializer.data)

    def post(self, request, format=None):
            Serializers = ClientSerializer(data=request.data)
            if Serializers.is_valid():
                Serializers.save()
                return Response(Serializers.data, status=status.HTTP_201_CREATED)
            return Response(Serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class ClientDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser | ReadOnly]
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    name = 'Client-detail'


class OrderFilter(FilterSet):
    min_price = NumberFilter(field_name='price', lookup_expr='gte')
    max_price = NumberFilter(field_name='price', lookup_expr='lte')
    client_name = AllValuesFilter(field_name='Order__client_client')

    class Meta:
        model = Order
        fields = ['min_price', 'max_price', 'client_name']


class OrdersList(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser | ReadOnly]
    name = 'Orders'
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_class = OrderFilter

    def get_object(self, pk):
            try:
                return Order.objects.get(pk=pk)
            except Order.DoesNotExist:
                raise Http404

    def get(self, request, format=None):
            Orders = Order.objects.all()
            Serializer = OrderSerializer(Orders, many=True)
            return Response(Serializer.data)

    def post(self, request, format=None):
            Serializers = OrderSerializer(data=request.data)
            if Serializers.is_valid():
                Serializers.save()
                return Response(Serializers.data, status=status.HTTP_201_CREATED)
            return Response(Serializers.errors, status=status.HTTP_400_BAD_REQUEST)




class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = Order
    name = 'Order-detail'


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({'book-categories': reverse(GenreList.name, request=request),
                         'books': reverse(BookList.name, request=request),
                         'clients': reverse(ClientList.name, request=request),
                         'orders': reverse(OrdersList.name, request=request),
                         'authors': reverse(AuthorList.name, request=request)
})


# class BookList(generics.ListCreateAPIView):
#     queryset = Book.objects.all()
#     name = 'Books'
#     serializer_class = BookSerializer
#
# class AuthorList(generics.ListCreateAPIView):
#     queryset = Author.objects.all()
#     name = 'Authors'
#     serializer_class = AuthorSerializer
#
# class GenreList(generics.ListCreateAPIView):
#     queryset = Genre.objects.all()
#     name = 'Genres'
#     serializer_class = GenreSerializer
#
# class ClientList(generics.ListCreateAPIView):
#     queryset = Client.objects.all()
#     name = 'Clients'
#     serializer_class = ClientSerializer
#
# class OrdersList(generics.ListCreateAPIView):
#     queryset = Order.objects.all()
#     name = 'Orders'
#     serializer_class = OrderSerializer

