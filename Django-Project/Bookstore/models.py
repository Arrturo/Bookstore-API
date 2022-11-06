from django.db import models

# Create your models here.

class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    price = models.FloatField()
    description = models.TextField()
    publisher = models.CharField(max_length=45)
    number_of_copies = models.IntegerField()
    year_of_publication = models.DateField()
    genre_genre = models.ForeignKey('Genre', on_delete=models.SET_NULL, null=True)
    section_section = models.ForeignKey('Section', on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.title

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    client_client = models.ForeignKey('Client', on_delete=models.SET_NULL, null=True)
    book_book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    purchase_date = models.DateField()

    def __str__(self):
        return self.client_client.title

class Author(models.Model):
    author_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)

    def __str__(self):
        return self.name + ' ' + self.last_name

class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    birth_date = models.DateField()
    city = models.CharField(max_length=45)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Section(models.Model):
    section_id = models.AutoField(primary_key=True)
    section_name = models.CharField(max_length=45)

    def __str__(self):
        return self.section_name

class Genre(models.Model):
    genre_id = models.AutoField(primary_key=True)
    genre = models.CharField(max_length=50)
    def __str__(self):
        return self.genre
    
    def __str__(self) -> str:
        return self.genre