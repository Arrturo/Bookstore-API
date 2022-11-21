from django.contrib import admin
from django.urls import include, path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', BookList.as_view(), name=BookList.name),
    path('Authors/', AuthorList.as_view(), name=AuthorList.name),
    path('Genres/', GenreList.as_view(), name=GenreList.name),
    path('Clients/', ClientList.as_view(), name=ClientList.name),
    path('Orders/', OrdersList.as_view(), name=OrdersList.name)
    ]
