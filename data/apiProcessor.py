import json
import os
import random

import pandas as pd
import requests


def get_json(subject):
    """
    get 10 book json by subject
    """
    url = f"https://www.googleapis.com/books/v1/volumes?q=subject:{subject}"
    res = requests.get(url)
    path = os.path.join(os.path.dirname(__file__), f"resources/base_json/{subject}.json")
    with open(path, "w", encoding='utf-8') as f:
        json.dump(res.json(), f, indent=4, ensure_ascii=False)


def preprocess_json():
    """
    get unqine values in all json
    etc. authors Language
    """

    def create_output(item):
        output = {}
        output["title"] = item['volumeInfo']['title']
        try:
            output["authors"] = item['volumeInfo']['authors']
        except:
            output["authors"] = ["none"]
        output["publisher"] = item['volumeInfo']['publisher']
        try:
            output["publishedDate"] = item['volumeInfo']['publishedDate']
        except:
            output["publishedDate"] = "none"
        output["description"] = item['volumeInfo']['description']
        try:
            output["isbn"] = list(filter(lambda industryIdentifier: industryIdentifier['type'] == 'ISBN_13'
                                         , item['volumeInfo']['industryIdentifiers']))[0]['identifier']
        except:
            output["isbn"] = random.randint(100000000000, 9999999999999)
        output["image"] = item['volumeInfo']['imageLinks']['thumbnail']
        output["language"] = item['volumeInfo']['language']
        return output

    for subject in ["ART", "EDUCATION", "DESIGN", "FICTION", "NATURE", "MUSIC", "HISTORY", "RELIGION", "SCIENCE",
                    "TRAVEL"]:
        base_path = os.path.join(os.path.dirname(__file__), f"resources/base_json/{subject}.json")
        preprocess_path = os.path.join(os.path.dirname(__file__), f"resources/preprocess_json/{subject}.json")
        with open(base_path, "r", encoding='utf-8') as fr:
            data = json.load(fr)
        items = list(map(lambda item: create_output(item), data['items']))
        with open(preprocess_path, "w", encoding='utf-8') as fw:
            json.dump(items, fw, indent=4, ensure_ascii=False)


def get_unqine_value(column):
    """
    Get unqine values in all csv
    ['title', 'authors', 'publisher', 'publishedDate', 'description', 'isbn', 'image', 'language','genre]
    """
    if column in ['authors', 'language']:
        values = []
        for subject in ["ART", "EDUCATION", "DESIGN", "FICTION", "NATURE", "MUSIC", "HISTORY", "RELIGION", "SCIENCE",
                        "TRAVEL"]:
            preprocess_path = os.path.join(os.path.dirname(__file__), f"resources/preprocess_json/{subject}.json")
            with open(preprocess_path, "r", encoding='utf-8') as fr:
                data = json.load(fr)
            values += list(map(lambda subdata: subdata[column], data))
    else:
        values = list(map(lambda word: word.lower(),
                          ["ART", "EDUCATION", "DESIGN", "FICTION", "NATURE", "MUSIC", "HISTORY", "RELIGION", "SCIENCE",
                           "TRAVEL"]))
    return list(set(values))


def create_book_table():
    """
    create book table
    """
    title = []
    author = []
    genre = []
    language = []
    isbn = []
    summary = []
    image = []
    for subject in ["ART", "EDUCATION", "DESIGN", "FICTION", "NATURE", "MUSIC", "HISTORY", "RELIGION", "SCIENCE",
                    "TRAVEL"]:
        preprocess_path = os.path.join(os.path.dirname(__file__), f"resources/preprocess_json/{subject}.json")
        with open(preprocess_path, "r", encoding='utf-8') as fr:
            data = json.load(fr)
        for book in data:
            title.append(book['title'])
            author.append(book['authors'][0])
            summary.append(book['description'])
            isbn.append(book['isbn'])
            image.append(book['image'])
            language.append(book['language'])
            genre.append(subject.lower())
    df = pd.DataFrame({
        "title": title,
        "author": author,
        "genre": genre,
        "language": language,
        "isbn": isbn,
        "summary": summary,
        "image": image,
    })
    df.to_csv(os.path.join(os.path.dirname(__file__), f"book.csv"), index=False)


def create_table():
    """
    author,genre,language
    """
    for model in ["author","genre","language"]:
        table = pd.DataFrame()
        df = pd.read_csv(os.path.join(os.path.dirname(__file__), f"book.csv"))
        table['name']=list(set(df[model]))
        table.to_csv(os.path.join(os.path.dirname(__file__), f"resources/final_csv/{model}.csv"),index=False)



if __name__ == '__main__':
    create_table()
    # get json
    # for subject in ["ART","EDUCATION","DESIGN","FICTION","NATURE","MUSIC","HISTORY","RELIGION","SCIENCE","TRAVEL"]:
    #     get_json(subject)

    # preprocess json
    # preprocess_json()

    # create_book_table
    # create_book_table()
    pass
