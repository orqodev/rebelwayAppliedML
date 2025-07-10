import pytest
from library.book import Book

def test_book_creation():
    """Test that a book can be created with the correct properties."""
    book = Book("1984", "George Orwell", "dystopian fiction")
    assert book.title == "1984"
    assert book.author == "George Orwell"
    assert book.genre == "dystopian fiction"
    assert book.available == True
    assert len(book.id) == 6

def test_book_availability():
    """Test that the availability status works correctly."""
    book = Book("Pride and Prejudice", "Jane Austen", "romance", False)
    assert book.available == False
    assert book.status == "Checked Out"

def test_book_search_string():
    """Test that the search string is correctly formatted."""
    book = Book("The Great Gatsby", "F. Scott Fitzgerald", "fiction")
    assert book.search_string == "The Great Gatsby F. Scott Fitzgerald fiction"

def test_book_status():
    """Test that the status property returns correct values."""
    available_book = Book("Available Book", "Author", "genre", True)
    checked_out_book = Book("Checked Out Book", "Author", "genre", False)
    
    assert available_book.status == "Available"
    assert checked_out_book.status == "Checked Out"