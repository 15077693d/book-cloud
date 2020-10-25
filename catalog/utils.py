import pandas as pd

from catalog.models import *

# books
genres_dict = dict(zip(['all', 'art', 'education', 'design', 'fiction', 'nature', 'music',
                        'history', 'religion', 'science', 'travel'],
                       ['隨書雲漂', "藝術", "教育", "設計", "科幻", "自然", "音樂", "歷史", "宗教", "科學", "旅遊"]))


def books_2_three_books_dict(books):
    genres = ['art', 'education', 'design', 'fiction', 'nature', 'music',
              'history', 'religion', 'science', 'travel']
    chi_genres = ["藝術", "教育", "設計", "科幻", "自然", "音樂", "歷史", "宗教", "科學", "旅遊"]
    three_books_dict = {}
    for i in range(len(genres)):
        three_books_dict[genres[i]] = {
            "books": list(filter(lambda book: book.genre.all()[0].name == genres[i], books))[:3],
            "chinese": chi_genres[i]
        }

    return three_books_dict


# csv
def add_csv_2_db(csv, model_name):
    """
    add csv to db
    """
    df = pd.read_csv(csv)
    num_of_row = len(df)
    for i in range(num_of_row):
        row = df[i:i + 1][:]
        if (model_name == "language"):
            language = Language(name=list(row['name'])[0])
            language.save()
        if (model_name == "genre"):
            genre = Genre(name=list(row['name'])[0])
            genre.save()
        if (model_name == "author"):
            author = Author(name=list(row['name'])[0])
            author.save()
        if (model_name == "book"):
            book = Book(title=list(row['title'])[0],
                        author=Author.objects.get(name=list(row['author'])[0]),
                        isbn=list(row['isbn'])[0],
                        summary=list(row['summary'])[0],
                        image=list(row['image'])[0],
                        language=Language.objects.get(name=list(row['language'])[0]))
            book.save()
            book.genre.add(Genre.objects.get(name=list(row["genre"])[0]))
            book.save()
            # if (model_name == "bookInstance"):
            #     bookInstance =
            #     bookInstance.save()


def get_page_selected_items(page, num_of_item_each_page, items):
    if page == 1:
        prevPage = page
    else:
        prevPage = page - 1
    # 8 -> 1 16 -> 2
    if len(items) % num_of_item_each_page == 0:
        max = len(items) // num_of_item_each_page
    else:
        # 9 -> 2 18 -> 3
        max = len(items) // num_of_item_each_page + 1
    if page == max:
        nextPage = page
    else:
        nextPage = page + 1
    start_i = (page - 1) * num_of_item_each_page
    end_i = (page) * num_of_item_each_page

    return [prevPage, nextPage, items[start_i:end_i]]
