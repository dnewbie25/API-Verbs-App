from typing import Optional
import functions as fn
from fastapi.middleware.cors import CORSMiddleware

from fastapi import FastAPI

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    "http://127.0.0.1:5500",
    "https://api-verbs-app.onrender.com",
    "https://api-verbs-app.netlify.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
async def get_book(book_id: str):
    """
    Retrieves a book by its ID.

    Args:
        book_id: The ID of the book to retrieve.
        all: If you type 'all', then it will retrieve all books

    Returns:
        A dictionary representing the book with the matching ID.
    """
    return fn.get_book_by_id(book_id, BOOKS)

@app.post("/post/{book}")
async def post_book(book: str):
    """
    Adds a new book to the BOOKS list.

    Args:
        book (str): A string containing the book's id, title, author, and category, separated by commas. For example:
        7, Harry Potter and the Azkaban Hollows, JK Rowling, Fantasy

    Returns:
        str: A success message indicating that the book has been added.
    """
    arr = book.split(',')
    BOOKS.append({
        'book_id':int(arr[0].strip()),
        'title':arr[1].strip(),
        'author':arr[2].strip(),
        'category':arr[3].strip(),
    })
    return BOOKS

@app.put("/put/{book}")
async def put_book(book: str):
    """
    Updates an existing book in the BOOKS list.

    Args:
        book (str): A string containing the id of the book you want to modify, title, author, and category, separated by commas. For example: 
        7, Harry Potter and the Deadly Hollows, JK Rowling, Fantasy

    Returns:
        str: A success message indicating that the book has been modified.
    """
    arr = book.split(',')
    new_book = {
        'book_id':int(arr[0].strip()),
        'title':arr[1].strip(),
        'author':arr[2].strip(),
        'category':arr[3].strip(),
    }
    for item in range(len(BOOKS)):
        if BOOKS[item]['book_id'] == new_book['book_id']:
            BOOKS[item] = new_book
    return "Book modified"

@app.delete("/delete/")
async def delete_book(books: str):
    """
    Deletes one or more books from the BOOKS list by their IDs.

    Args:
        books (str): A comma-separated string of book IDs to delete.

    Returns:
        str: A success message indicating that the book has been deleted.
    """
    BOOKS[:] = fn.delete_book_by_id(books, BOOKS)
    return "Book deleted"
