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
    
def delete_book_by_id(ids: str, books: list):
  """
  Deletes books by their IDs from a list of books.

  Args:
    ids (str): A comma-separated string of book IDs to delete.
    books (list): A list of dictionaries representing books, each with a 'book_id' key.

  Returns:
    list: The updated list of books with the specified IDs removed.
  """
  ids_list = ids.split(',')
  print(ids_list)
  books[:] = list(filter(lambda book: str(book['book_id']) not in ids_list, books))
  return books
