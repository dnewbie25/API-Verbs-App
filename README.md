# API for practicing GET, POST, PUT, DELETE

This API is just for practicing the 4 basic verbs of a RESTful API (GET, POST, PUT, DELETE). It is not intended to be a real API.

> The API URL is this one: _[https://api-verbs-app.onrender.com](https://api-verbs-app.onrender.com)_

> The API interactive documentation created by FastAPI can be found here _[API Documentation](https://api-verbs-app.onrender.com/docs)_

## Endpoints

### GET

* `/get/{book_id}`: Retrieves a book by its ID. The ID is a natural number. Default books go from ID `1` to `6`.
* `/get/all`: Retrieves all books.

### POST

* `/post/{book}`: Adds a new book to the list. The book is passed as a string containing the book's id, title, author, and category, separated by commas, i.e., "7,Harry Potter and the Deadly Hollows,JK Rowling,Fantasy".
The `POST` method does not do any validation or conversion. As long as there are those 4 elements sepparated by commas, it will work.

### PUT

* `/put/{book}`: Updates an existing book in the list. The book is passed as a string containing the book's id, title, author, and category, separated by commas. It will then modify the data using the id to find the book.

### DELETE

* `/delete/`: Deletes one or more books from the list by their IDs.

## Usage

You can use any HTTP client to interact with this API, although the main goal is to use a Javascript app to interact with this API.
