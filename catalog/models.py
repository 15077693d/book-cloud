from django.contrib.auth.models import User
from django.db import models


class Friend(models.Model):
    friend_STATUS = [
        ('w', 'waiting'),
        ('r', 'rejected'),
        ('a', 'available'),
    ]
    status = models.CharField(max_length=1, default='w', choices=friend_STATUS)
    receiver = models.OneToOneField(User, related_name='receiver_friend_set', on_delete=models.CASCADE)
    requester = models.OneToOneField(User, related_name='requester_friend_set', on_delete=models.CASCADE)

class Language(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateTimeField(null=True, blank=True)
    date_of_death = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    genre = models.ManyToManyField(Genre)
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True)
    isbn = models.CharField(max_length=13,
                            help_text="<a href='https://zh.wikipedia.org/zh-hk/%E5%9B%BD%E9%99%85%E6%A0%87%E5%87%86%E4%B9%A6%E5%8F%B7'>click here for isbn detail<a>")
    summary = models.TextField()
    image = models.TextField(null=True)

    def display_genre(self):
        """Create a string for the Genre. This is required to display genre in Admin."""
        return ', '.join(genre.name for genre in self.genre.all()[:3])

    display_genre.short_description = 'Genre'

    def __str__(self):
        return self.title


def holder_default():
    return User.objects.get(username="test1@gmail.com")


class BookInstance(models.Model):
    LOAN_STATUS = [
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    ]
    borrower = models.ForeignKey(User, related_name='borrower_bookinstance_set', on_delete=models.CASCADE, null=True,
                                 blank=True)
    holder = models.ForeignKey(User, related_name='holder_bookinstance_set', on_delete=models.SET_NULL, null=True,
                               default=holder_default)
    bookers = models.ManyToManyField(User, blank=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True)
    due_back = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=1, default='m', choices=LOAN_STATUS)
    history = models.ManyToManyField(User, related_name='history_bookinstance_set', blank=True)

    def display_book(self):
        return self.book.title

    def __str__(self):
        return f"{self.book} {self.status}"
