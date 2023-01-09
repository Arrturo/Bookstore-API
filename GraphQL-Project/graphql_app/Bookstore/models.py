from django.db import models
import datetime
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
# Create your models here.

def Date_validation(date:datetime):
    if date > datetime.date.today():
        raise ValidationError(_("Data nie może być nowsza niż dzisiejsza data."))


def Price_validation(price):
    if price < 0:
        raise ValidationError(_("Cena nie może być wartością ujemną."))

    if round(price, 2) != price:
        raise ValidationError(_("Cena może być sprecyzowana do jednego grosza."))


def Name_validation(name: str):
    # x = str(name).replace(' ', '')
    # if not x.isalpha():
    #     raise ValidationError(_("Dane mogą zwierać tylko litery."))
    pass


class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True, validators=[Name_validation])
    price = models.FloatField(validators=[Price_validation])
    description = models.TextField()
    publisher = models.CharField(max_length=45)
    number_of_copies = models.IntegerField()
    year_of_publication = models.DateField(validators=[Date_validation])
    genre_genre = models.ForeignKey('Genre', on_delete=models.SET_NULL, null=True, validators=[Name_validation])

    def __str__(self):
        return self.title

class Author(models.Model):
    author_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, validators=[Name_validation])
    last_name = models.CharField(max_length=45, validators=[Name_validation])

    def __str__(self):
        return self.name + ' ' + self.last_name


class Genre(models.Model):
    genre_id = models.AutoField(primary_key=True)
    genre = models.CharField(max_length=50, validators=[Name_validation])
    def __str__(self):
        return self.genre