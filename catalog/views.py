# Create your views here.
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect

from catalog.utils import *


def user(request,username):
    # username = request.session['user']
    friend_names = []
    receive_friend = Friend.objects.filter(receiver__username=username)
    for friend in receive_friend:
        friend_names.append(friend.requester.username)
    request_friend = Friend.objects.filter(requester__username=username)
    for friend in request_friend:
        friend_names.append(friend.receiver.username)
    user_object = User.objects.get_by_natural_key(username=username)
    hold_bookInstances=BookInstance.objects.filter(holder__username=username)
    hold_book = {}
    for bookInstance in hold_bookInstances:
        hold_book[bookInstance.book.id] = bookInstance.book.image
    read_bookInstances=BookInstance.objects.filter(history__in=[user_object])
    read_book = {}
    for bookInstance in read_bookInstances:
        read_book[bookInstance.book.id] = bookInstance.book.image
    return render(request, 'profile.html',context={"friends":friend_names,
                                                   "hold_book":hold_book,
                                                   "read_book":read_book,
                                                   "username":username})


def book(request, book_id):
    book_object = Book.objects.get(pk=book_id)
    book_instance_objects = BookInstance.objects.filter(book__title=book_object.title)
    return render(request, 'book.html', context={"book": book_object, "book_instances": book_instance_objects})


def books(request, genre, page):
    if genre != 'all':
        genre_object = Genre.objects.get(name=genre)
        book_objects = Book.objects.filter(genre__in=[genre_object])
    else:
        book_objects = Book.objects.all()
    num_of_book_each_page = 5
    prevPage, nextPage, selected_book_objects = get_page_selected_items(page=page,
                                                                        num_of_item_each_page=num_of_book_each_page,
                                                                        items=book_objects)
    return render(request, 'books.html', context={"genre": genre, "chinese_genre": genres_dict[genre],
                                                  "prevPage": prevPage, "nextPage": nextPage,
                                                  'books': selected_book_objects})


def index(request):
    books = Book.objects.all()
    context = {
        "three_books_dict": books_2_three_books_dict(books)
    }
    return render(request, 'index.html', context=context)


def author(request, author_name, page):
    book_objects = Book.objects.filter(author__name=author_name)
    num_of_book_each_page = 8
    prevPage, nextPage, selected_book_objects = get_page_selected_items(page=page,
                                                                        num_of_item_each_page=num_of_book_each_page,
                                                                        items=book_objects)
    return render(request, 'author.html', context={
        "book_objects": selected_book_objects,
        "prevPage": prevPage,
        "nextPage": nextPage
    })


def authors(request, page):
    author_objects = Author.objects.all()
    num_of_author_each_page = 10
    prevPage, nextPage, selected_author_objects = get_page_selected_items(page=page,
                                                                          num_of_item_each_page=num_of_author_each_page,
                                                                          items=author_objects)
    author_dict_list = []
    for author_object in selected_author_objects:
        author_dict = {}
        author_dict['name'] = author_object.name
        author_books = Book.objects.filter(author__name=author_object.name)
        author_genres = list(
            set(map(lambda book: genres_dict[book.genre.all()[0].name], author_books)))
        author_dict['book_count'] = author_books.count()
        author_dict['fields'] = '、'.join(author_genres)
        author_dict_list.append(author_dict)
    return render(request, 'authors.html', context={
        "author_dict_list": author_dict_list,
        "prevPage": prevPage,
        "nextPage": nextPage
    })


def signup_login_logout(request):
    if 'signup' in request.POST:
        user = User.objects.create_user(email=request.POST['email'], username=request.POST['username'],
                                        password=request.POST['password'])
        user.save()
        request.session['user'] = user.username
    elif 'login' in request.POST:
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            request.session['user'] = user.username
        else:
            return redirect(request.POST['url'])
    else:
        request.session['user'] = False
        return redirect('/')
    return redirect(request.POST['url'])


def csv(request):
    if request.method == 'POST':
        csv_result = "-> "
        if 'instance' in request.POST:
            for book in Book.objects.all():
                bookInstance = BookInstance(book=book, status="a")
                bookInstance.save()
            csv_result += f"book instance added..."
        for item in ['language', 'genre', 'author', 'book']:
            if item in request.FILES:
                file = request.FILES[item]
                add_csv_2_db(file, item)
                csv_result += f"{item} "

        return render(request, 'csv.html', {
            'uploaded_file_url': csv_result
        })

    return render(request, 'csv.html')
