import pytest
import json
import os
from library.library_system import LibrarySystem
from library.book import Book

@pytest.fixture
def test_database():
    """Create a temporary database file for testing."""
    db_path = "test_database.json"
    with open(db_path, "w") as f:
        json.dump({"Books": {}}, f)
    yield db_path
    # Clean up after the test
    if os.path.exists(db_path):
        os.remove(db_path)

def test_library_creation(test_database):
    """Test that a library can be created with the correct properties."""
    library = LibrarySystem(test_database)
    assert library.database_path == test_database

def test_add_book_to_library(test_database):
    """Test that a book can be added to the library."""
    library = LibrarySystem(test_database)
    book = Book("1984", "George Orwell", "dystopian fiction")
    library.add_book_to_library(book)

    # Check that the book was added to the database
    data = library.get_all_books()
    assert len(data["Books"]) == 1
    assert data["Books"][book.id]["title"] == "1984"
    assert data["Books"][book.id]["author"] == "George Orwell"
    assert data["Books"][book.id]["genre"] == "dystopian fiction"
    assert data["Books"][book.id]["available"] == True

def test_checkout_book(test_database):
    """Test that a book can be checked out."""
    library = LibrarySystem(test_database)
    book = Book("Pride and Prejudice", "Jane Austen", "romance")
    library.add_book_to_library(book)

    # Checkout the book
    library.checkout_book("Pride and Prejudice")

    # Check that the book is now unavailable
    data = library.get_all_books()
    assert data["Books"][book.id]["available"] == False

def test_return_book(test_database):
    """Test that a book can be returned."""
    library = LibrarySystem(test_database)
    book = Book("The Great Gatsby", "F. Scott Fitzgerald", "fiction")
    library.add_book_to_library(book)

    # Checkout and then return the book
    library.checkout_book("The Great Gatsby")
    library.return_book("The Great Gatsby")

    # Check that the book is now available again
    data = library.get_all_books()
    assert data["Books"][book.id]["available"] == True

def test_get_available_books_count(test_database):
    """Test that the available books count is calculated correctly."""
    library = LibrarySystem(test_database)
    book1 = Book("Book 1", "Author 1", "genre1")
    book2 = Book("Book 2", "Author 2", "genre2")
    library.add_book_to_library(book1)
    library.add_book_to_library(book2)

    # Initially both books should be available
    assert library.get_available_books_count() == 2

    # Checkout one book
    library.checkout_book("Book 1")
    assert library.get_available_books_count() == 1
