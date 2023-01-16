import graphene
from graphene_django import DjangoObjectType
from .models import Book, Author, Genre, Order, Client


class BookType(DjangoObjectType):
    class Meta:
        model = Book
        fields = (
            'book_id',
            'title',
            'author',
            'price',
            'description',
            'publisher',
            'number_of_copies',
            'year_of_publication',
            'genre_genre',
        )


class AuthorType(DjangoObjectType):
    class Meta:
        model = Author
        fields = (
            'author_id',
            'name',
            'last_name',
        )


class GenreType(DjangoObjectType):
    class Meta:
        model = Genre
        fields = (
            'genre_id',
            'genre',
        )


class OrderType(DjangoObjectType):
    class Meta:
        model = Order
        fields = (
            'order_id',
            'client_client',
            'book_book',
            'purchase_date',
            'price',
        )


class ClientType(DjangoObjectType):
    class Meta:
        model = Client
        fields = (
            'client_id',
            'name',
            'last_name',
            'birthdate',
            'city',
            'address',
        )


class Query(graphene.ObjectType):
    books = graphene.List(BookType)
    authors = graphene.List(AuthorType)
    genres = graphene.List(GenreType)
    orders = graphene.List(OrderType)
    clients = graphene.List(ClientType)

    def resolve_books(self, info, **kwargs):
        return Book.objects.all()

    def resolve_authors(self, info, **kwargs):
        return Author.objects.all()

    def resolve_genres(self, info, **kwargs):
        return Genre.objects.all()

    def resolve_orders(self, info, **kwargs):
        return Order.objects.all()

    def resolve_clients(self, info, **kwargs):
        return Client.objects.all()


class BookInput(graphene.InputObjectType):
    title = graphene.String()
    author = graphene.String()
    price = graphene.Float()
    description = graphene.String()
    publisher = graphene.String()
    number_of_copies = graphene.Int()
    year_of_publication = graphene.Date()
    genre_genre = graphene.String()


class UpdateBook(graphene.Mutation):
    class Arguments:
        book_id = graphene.ID()
        input = BookInput(required=False)

    book = graphene.Field(BookType)

    @classmethod
    def mutate(cls, root, info, book_id, input):
        book = Book.objects.get(book_id=book_id)
        book.title = input.title,
        book.author = input.author,
        book.price = input.price,
        book.description = input.description,
        book.publisher = input.publisher,
        book.number_of_copies = input.number_of_copies,
        book.year_of_publication = input.year_of_publication,
        book.genre_genre = input.genre_genre,
        book.save()
        return UpdateBook(book=book)


class CreateBook(graphene.Mutation):
    class Arguments:
        input = BookInput(required=False)

    book = graphene.Field(BookType)

    @classmethod
    def mutate(cls, root, info, input):
        book = Book()
        book.title = input.title,
        book.author = input.author,
        book.price = input.price,
        book.description = input.description,
        book.publisher = input.publisher,
        book.number_of_copies = input.number_of_copies,
        book.year_of_publication = input.year_of_publication,
        book.genre_genre = input.genre_genre,
        book.save()
        return CreateBook(book=book)


class DeleteBook(graphene.Mutation):
    class Arguments:
        book_id = graphene.ID()

    book = graphene.Field(BookType)

    @classmethod
    def mutate(cls, root, info, book_id):
        book = Book.objects.get(book_id=book_id)
        book.delete()


class UpdateGenre(graphene.Mutation):
    class Arguments:
        genre_id = graphene.ID()
        genre_name = graphene.String()

    genre = graphene.Field(GenreType)

    @classmethod
    def mutate(cls, root, info, genre_id, genre_name):
        genre = Genre.objects.get(pk=genre_id)
        genre.genre = genre_name
        genre.save()

        return UpdateGenre(genre=genre)


class CreateGenre(graphene.Mutation):
    class Arguments:
        genre = graphene.String()

    genre = graphene.Field(GenreType)

    @classmethod
    def mutate(cls, root, info, genre):
        genre = Genre(genre=genre)
        genre.save()

        return CreateGenre(genre=genre)


class DeleteGenre(graphene.Mutation):
    class Arguments:
        genre_id = graphene.ID()

    genre = graphene.Field(GenreType)

    @classmethod
    def mutate(cls, root, info, genre_id):
        genre = Genre.objects.get(pk=genre_id)
        genre.delete()


class UpdateAuthor(graphene.Mutation):
    class Arguments:
        author_id = graphene.ID()
        name = graphene.String()
        last_name = graphene.String()

    author = graphene.Field(AuthorType)

    @classmethod
    def mutate(cls, root, info, author_id, name, last_name):
        author = Author.objects.get(pk=author_id)
        author.name = name
        author.last_name = last_name
        author.save()

        return UpdateAuthor(author=author)


class CreateAuthor(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        last_name = graphene.String()

    author = graphene.Field(AuthorType)

    @classmethod
    def mutate(cls, root, info, name, last_name):
        author = Author()
        author.name = name
        author.last_name = last_name
        author.save()

        return CreateAuthor(author=author)


class DeleteAuthor(graphene.Mutation):
    class Arguments:
        author_id = graphene.ID()

    author = graphene.Field(AuthorType)

    @classmethod
    def mutate(cls, root, info, author_id):
        author = Author.objects.get(pk=author_id)
        author.delete()


class OrderInput(graphene.InputObjectType):
    client_client = graphene.String()
    book_book = graphene.String()
    purchase_date = graphene.Date()
    price = graphene.Float()


class CreateOrder(graphene.Mutation):
    class Arguments:
        input = OrderInput(required=True)

    order = graphene.Field(OrderType)

    @classmethod
    def mutate(cls, root, info, input):
        order = Order()
        order.client_client = input.client_client,
        order.book_book = input.book_book,
        order.purchase_date = input.purchase_date,
        order.price = input.price,

        order.save()
        return CreateOrder(order=order)


class UpdateOrder(graphene.Mutation):
    class Arguments:
        order_id = graphene.ID()
        input = OrderInput(required=False)

    order = graphene.Field(OrderType)

    @classmethod
    def mutate(cls, root, info, order_id, input):
        order = Order.objects.get(order_id=order_id)
        order.client_client = input.client_client,
        order.book_book = input.book_book,
        order.purchase_date = input.purchase_date,
        order.price = input.price,

        order.save()
        return UpdateOrder(order=order)


class DeleteOrder(graphene.Mutation):
    class Arguments:
        order_id = graphene.ID()

    order = graphene.Field(OrderType)

    @classmethod
    def mutate(cls, root, info, order_id):
        order = Order.objects.get(pk=order_id)
        order.delete()


class CreateClient(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        last_name = graphene.String()
        email = graphene.String()
        phone = graphene.String()

    client = graphene.Field(ClientType)

    @classmethod
    def mutate(cls, root, info, name, last_name, email, phone):
        client = Client()
        client.name = name
        client.last_name = last_name
        client.email = email
        client.phone = phone
        client.save()
        return CreateClient(client=client)


class UpdateClient(graphene.Mutation):
    class Arguments:
        client_id = graphene.ID()
        name = graphene.String()
        last_name = graphene.String()
        email = graphene.String()
        phone = graphene.String()

    client = graphene.Field(ClientType)

    @classmethod
    def mutate(cls, root, info, client_id, name, last_name, email, phone):
        client = Client.objects.get(pk=client_id)
        client.name = name
        client.last_name = last_name
        client.email = email
        client.phone = phone
        client.save()
        return UpdateClient(client=client)


class DeleteClient(graphene.Mutation):
    class Arguments:
        client_id = graphene.ID()

    client = graphene.Field(ClientType)

    @classmethod
    def mutate(cls, root, info, client_id):
        client = Client.objects.get(pk=client_id)
        client.delete()

class Mutation(graphene.ObjectType):
    update_book = UpdateBook.Field()
    create_book = CreateBook.Field()
    delete_book = DeleteBook.Field()

    update_genre = UpdateGenre.Field()
    create_genre = CreateGenre.Field()
    delete_genre = DeleteGenre.Field()

    update_author = UpdateAuthor.Field()
    create_author = CreateAuthor.Field()
    delete_author = DeleteAuthor.Field()

    create_order = CreateOrder.Field()
    update_order = UpdateOrder.Field()
    delete_order = DeleteOrder.Field()

    create_client = CreateClient.Field()
    update_client = UpdateClient.Field()
    delete_client = DeleteClient.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)