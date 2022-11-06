from django.contrib import admin

from Bookstore.models import *

# Register your models here.
admin.site.register(Book)
admin.site.register(Order)
admin.site.register(Author)
admin.site.register(Client)
admin.site.register(Section)
admin.site.register(Genre)
