from django.contrib import admin
from Bookstore.models import Book, Author, Genre, Order, Client

# Register your models here.
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Order)
admin.site.register(Client)