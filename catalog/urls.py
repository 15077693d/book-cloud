from django.urls import path

from catalog import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/<str:genre>/<int:page>', views.books, name='books'),
    path('csv', views.csv, name='csv'),
    path('book/<int:book_id>', views.book, name='book'),
    path('author/<str:author_name>/<int:page>', views.author, name='author'),
    path('authors/<int:page>', views.authors, name='authors'),
    path('signup_login_logout',views.signup_login_logout)
]
