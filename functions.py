def get_book_by_id(id, books: list):
  """
  Retrieves a book by its ID from a list of books.

  Args:
    id: The ID of the book to retrieve. If 'all', returns the entire list of books.
    books (list): A list of dictionaries representing books, each with a 'book_id' key.

  Returns:
    A dictionary representing the book with the matching ID, or the entire list of books if ID is 'all'.
  """
  if id == 'all':
    return books
  for book in books:
    if book['book_id'] == int(id):
      return book
    
def delete_book_by_id(ids: list, books: list):
  """
  Deletes books by their IDs from a list of books.

  Args:
    ids (list): A list of book IDs to delete.
    books (list): A list of dictionaries representing books, each with a 'book_id' key.

  Returns:
    list: The updated list of books with the specified IDs removed.
  """
  books = list(filter(lambda book: book['book_id'] not in ids, books))
  return books