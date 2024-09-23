from typing import Optional
import functions as fn

from fastapi import FastAPI, Query
from typing import List

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
async def get_book(book_id):
    """
    Retrieves a book by its ID.

    Args:
        book_id: The ID of the book to retrieve.

    Returns:
        A dictionary representing the book with the matching ID.
    """
    return fn.get_book_by_id(book_id, BOOKS)

@app.post("/post/{book}")
async def post_book(book: str):
    """
    Adds a new book to the BOOKS list.

    Args:
        book (str): A string containing the book's id, title, author, and category, separated by commas.

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
    return "Book added"

@app.put("/put/{book}")
async def put_book(book: str):
    """
    Updates an existing book in the BOOKS list.

    Args:
        book (str): A string containing the book's id, title, author, and category, separated by commas.

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
async def delete_book(books: List[int] = Query(...)):
    """
    Deletes one or more books from the BOOKS list by their IDs.

    Args:
        books (List[int]): A list of book IDs to delete.

    Returns:
        str: A success message indicating that the book has been deleted.
    """
    filtered_list = list(filter(lambda book: book['book_id'] not in books, BOOKS))
    BOOKS[:] = filtered_list
    return "Book deleted"