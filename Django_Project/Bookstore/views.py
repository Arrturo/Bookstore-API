from rest_framework import generics
from .serializers import *
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS
from rest_framework.reverse import reverse
from django_filters import AllValuesFilter, DateTimeFilter, NumberFilter, FilterSet
from .customperm import IsCurrentUserOwnerOrReadOnly, CurrentUserOwnerReadOnlyOrDenied

# Create your views here.



class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class BookFilter(FilterSet):
    from_price = NumberFilter(field_name="price", lookup_expr='gte')
    to_price = NumberFilter(field_name="price", lookup_expr='lte')
    class Meta:
        model = Book
        fields = ['from_price', 'to_price', 'title', 'author', 'price', 'genre_genre']


class BookList(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser | ReadOnly]
    name = 'Books'
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filterset_class = BookFilter
    search_fields = ['title']
    ordering_fields = ['title', 'author']


    # def get_object(self, pk):
    #     try:
    #         return Book.objects.get(id=pk)
    #     except Book.DoesNotExist:
    #         raise Http404
    #
    # def get(self, request, Format=None):
    #     Books = Book.objects.all()
    #     Serializer = BookSerializer(Books, many=True)
    #     return Response(Serializer.data)
    #
    # def post(self, request, Format=None):
    #     Serializer = BookSerializer(data=request.data)
    #     if Serializer.is_valid():
    #         Serializer.save()
    #         return Response(Serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(Serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser | ReadOnly]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    name = 'book-detail'


class AuthorList(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser | ReadOnly]
    name = 'Authors'
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    search_fields = ['name', 'last_name']
    ordering_fields = ['name', 'last_name']

    # def get_object(self, pk):
    #     try:
    #         return Author.objects.get(pk=pk)
    #     except Author.DoesNotExist:
    #         raise Http404
    #
    # def get(self, request, format=None):
    #     Authors = Author.objects.all()
    #     Serializer = AuthorSerializer(Authors, many=True)
    #     return Response(Serializer.data)
    #
    # def post(self, request, format=None):
    #     Serializer = AuthorSerializer(data=request.data)
    #     if Serializer.is_valid():
    #         Serializer.save()
    #         return Response(Serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(Serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser | ReadOnly]
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    name = 'author-detail'


class GenreList(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser | ReadOnly]
    name = 'Genres'
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

    # def get_object(self, pk):
    #     try:
    #         return Genre.objects.get(pk=pk)
    #     except Genre.DoesNotExist:
    #         raise Http404
    #
    # def get(self, request, format=None):
    #     Genres = Genre.objects.all()
    #     Serializer = GenreSerializer(Genres, many=True)
    #     return Response(Serializer.data)
    #
    # def post(self, request, format=None):
    #     Serializers = GenreSerializer(data=request.data)
    #     if Serializers.is_valid():
    #         Serializers.save()
    #         return Response(Serializers.data, status=status.HTTP_201_CREATED)
    #     return Response(Serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class GenreDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser | ReadOnly]
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    name = 'genre-detail'


class ClientFilter(FilterSet):
    from_birthdate = DateTimeFilter(field_name='birth_date', lookup_expr='gte')
    to_birthdate = DateTimeFilter(field_name='birth_date', lookup_expr='lte')

    class Meta:
        model = Client
        fields = ['from_birthdate', 'to_birthdate']


class ClientList(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser | ReadOnly]
    name = 'Clients'
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    search_fields = ['name', 'last_name']
    filterset_class = ClientFilter
    ordering_fields = ['last_name', 'birth_date']

    # def get_object(self, pk):
    #         try:
    #             return Client.objects.get(pk=pk)
    #         except Client.DoesNotExist:
    #             raise Http404
    #
    # def get(self, request, format=None):
    #         Clients = Client.objects.all()
    #         Serializer = ClientSerializer(Clients, many=True)
    #         return Response(Serializer.data)
    #
    # def post(self, request, format=None):
    #         Serializers = ClientSerializer(data=request.data)
    #         if Serializers.is_valid():
    #             Serializers.save()
    #             return Response(Serializers.data, status=status.HTTP_201_CREATED)
    #         return Response(Serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class ClientDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser | ReadOnly]
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    name = 'client-detail'


class OrderFilter(FilterSet):
    client_name = AllValuesFilter(field_name='owner')

    class Meta:
        model = Order
        fields = ['client_name']


class OrdersList(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser | CurrentUserOwnerReadOnlyOrDenied]
    name = 'orders'
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    ordering_fields = ['client_name']
    filterset_class = OrderFilter

    def get_queryset(self):
        if self.request.user.is_staff:
            return Order.objects.all()
        else:
            return Order.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    # def get_object(self, pk):
    #         try:
    #             return Order.objects.get(pk=pk)
    #         except Order.DoesNotExist:
    #             raise Http404
    #
    # def get(self, request, format=None):
    #         Orders = Order.objects.all()
    #         Serializer = OrderSerializer(Orders, many=True)
    #         return Response(Serializer.data)
    #
    # def post(self, request, format=None):
    #         Serializers = OrderSerializer(data=request.data)
    #         if Serializers.is_valid():
    #             Serializers.save()
    #             return Response(Serializers.data, status=status.HTTP_201_CREATED)
    #         return Response(Serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser | CurrentUserOwnerReadOnlyOrDenied]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    name = 'order-detail'


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({'book-categories': reverse(GenreList.name, request=request),
                         'books': reverse(BookList.name, request=request),
                         'clients': reverse(ClientList.name, request=request),
                         'orders': reverse(OrdersList.name, request=request),
                         'authors': reverse(AuthorList.name, request=request)
})



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