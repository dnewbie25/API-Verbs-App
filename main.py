from typing import Optional
import functions as fn

from fastapi import FastAPI

app = FastAPI()

BOOKS = [
    {'book_id':1,'title': 'Title 1', 'author': 'Author 1', 'category': 'science'},
    {'book_id':2,'title': 'Title 2', 'author': 'Author 2', 'category': 'science'},
    {'book_id':3,'title': 'Title 3', 'author': 'Author 3', 'category': 'history'},
    {'book_id':4,'title': 'Title 4', 'author': 'Author 4', 'category': 'math'},
    {'book_id':5,'title': 'Title 5', 'author': 'Author 5', 'category': 'math'},
    {'book_id':6,'title': 'Title 6', 'author': 'Author 6', 'category': 'math'}
]


@app.get("/home")
async def root():
    return {"message": "This is a basic API I created to simulate a real API with the 4 main verbs: GET, POST, PUT and DELETE"}

@app.get("/get/{book_id}")
def get_book(book_id):
    """
    Retrieves a book by its ID.

    Args:
        book_id: The ID of the book to retrieve.

    Returns:
        A dictionary representing the book with the matching ID.
    """
    return fn.get_book_by_id(book_id, BOOKS)

@app.post("/post/{book}")
def post_book(book: str):
    arr = book.split(',')
    BOOKS.append({
        'book_id':int(arr[0].strip()),
        'title':arr[1].strip(),
        'author':arr[2].strip(),
        'category':arr[3].strip(),
    })
    return "Book added"