from django.db import models
import datetime
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

#Validation Functions
def Date_validation(date:datetime):
    if date > datetime.date.today():
        raise ValidationError(_("Data nie może być nowsza niż dzisiejsza data."))


def Price_validation(price):
    if price < 0:
        raise ValidationError(_("Cena nie może być wartością ujemną."))

    if round(price, 2) != price:
        raise ValidationError(_("Cena może być sprecyzowana do jednego grosza."))


def Name_validation(name: str):
    x = str(name).replace(" ", "")
    if not x.isalpha():
        raise ValidationError(_("Dane mogą zwierać tylko litery."))

#Models
class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True, validators=[Name_validation])
    price = models.FloatField(validators=[Price_validation])
    description = models.TextField()
    publisher = models.CharField(max_length=45)
    number_of_copies = models.IntegerField()
    year_of_publication = models.DateField(validators=[Date_validation])
    genre_genre = models.ForeignKey('Genre', on_delete=models.SET_NULL, null=True,  validators=[Name_validation])
    section_section = models.ForeignKey('Section', on_delete=models.SET_NULL, null=True,  validators=[Name_validation])
    
    def __str__(self):
        return self.title

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    client_client = models.ForeignKey('Client', on_delete=models.SET_NULL, null=True)
    book_book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    purchase_date = models.DateField(validators=[Date_validation])
    price = models.FloatField(validators=[Price_validation], null=True)

    def __str__(self):
        return self.client_client.name

class Author(models.Model):
    author_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, validators=[Name_validation])
    last_name = models.CharField(max_length=45, validators=[Name_validation])

    def __str__(self):
        return self.name + ' ' + self.last_name

class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, validators=[Name_validation])
    last_name = models.CharField(max_length=45, validators=[Name_validation])
    birth_date = models.DateField(validators=[Date_validation])
    city = models.CharField(max_length=45, validators=[Name_validation])
    address = models.CharField(max_length=100)

    class Meta:
        ordering = ('last_name',)

    def __str__(self):
        return self.name

class Section(models.Model):
    section_id = models.AutoField(primary_key=True)
    section_name = models.CharField(max_length=45)

    def __str__(self):
        return self.section_name

class Genre(models.Model):
    genre_id = models.AutoField(primary_key=True)
    genre = models.CharField(max_length=50, validators=[Name_validation])
    def __str__(self):
        return self.genre