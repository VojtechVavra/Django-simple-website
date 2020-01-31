from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.BookIndex.as_view(), name="book_index"),
    path("home/", views.BookIndex.as_view(), name="book_index"),
    path("<int:pk>/book_detail/", views.CurrentBookView.as_view(), name="book_detail"),
    #path("<int:pk>/author_detail/", views.AuthorIndex.as_view(), name="author_detail"),
    path("<int:pk>/author_detail/", views.CurrentAuthorView.as_view(), name="author_detail"),
    path("add_book/", views.AddBook.as_view(), name="add_book"),
    path("add_genre/", views.AddGenre.as_view(), name="add_genre"),
    path("add_author/", views.AddAuthor.as_view(), name="add_author"),
]