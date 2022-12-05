from django.contrib import admin
from django.urls import include, path
from .views import *
from django.contrib.admin.views.decorators import staff_member_required


urlpatterns = [
    path('admin/', admin.site.urls),
    path('Books/', BookList.as_view(), name=BookList.name),
    path('Books/<int:pk>', BookDetail.as_view(), name=BookDetail.name),
    path('Authors/', AuthorList.as_view(), name=AuthorList.name),
    path('Authors/<int:pk>', AuthorDetail.as_view(), name=BookDetail.name),
    path('Genres/',  GenreList.as_view(), name=GenreList.name),
    path('Genres/<int:pk>', GenreDetail.as_view(), name=BookDetail.name),
    path('Clients/', staff_member_required(ClientList.as_view()), name=ClientList.name),
    path('Clients/<int:pk>', ClientDetail.as_view(), name=BookDetail.name),
    path('Orders/', staff_member_required(OrdersList.as_view()), name=OrdersList.name),
    path('Orders/<int:pk>', OrderDetail.as_view(), name=BookDetail.name),
    path('', views.ApiRoot.as_view(), name=views.ApiRoot.name)]