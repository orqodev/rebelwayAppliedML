import json
from dataclasses import dataclass, field

from library.file_io import Fstream
from library.random_number_utils import RandomUtils
from library.book import Book


@dataclass
class LibrarySystem:
    database_path: str

    def get_all_books(self, verbose=0)->dict:
        """
        Reads and returns a hash map with all the available books
        Args:
            if verbose is set 1, it will print all the books.
        Returns:
            dict: a hash map with all the books in the database
        """
        data_file = Fstream.load_json_files(self.database_path)

        try:
            if verbose == 1:
                Fstream.print_json_structure(data_file)
                return data_file
            else:
                return data_file
        except:
            raise ValueError("The value for the verbose as to be 0 or 1")

    def search_books(self,query:str)->list[Book]:
        """
        Searches books in the database
        Args:
            query: search query
        Returns:
            list[Book]: a list of Book
        """
        data = Fstream.load_json_files(self.database_path)
        matching_books = []
        for book_id, book_data in data["Books"].items():
            book = Book(title=book_data["title"], author=book_data["author"], genre=book_data["genre"], available=book_data["available"], id=book_id)
            if query.lower() in book.search_string.lower():
                matching_books.append(book)

        if len(matching_books) == 0:
            print("No matching books found")
        else:
            for book in matching_books:
                print(f"Found: {book.title} by {book.author} ({book.genre}) - {book.status}")

        return matching_books

    def get_total_books_count(self)->int:
        """
        Returns the total number of books in the library.

        Returns:
            int: the total number of books in the library
        """
        data = self.get_all_books()
        return len(data["Books"].items())

    def add_book_to_library(self,book:Book):
        """
        Adds a book to the library and update the database json file.
        Checks if the book already exists (same title and author) before adding.

        Args:
            book (Book): the book to add to the library
        """

        data = self.get_all_books()

        # Check if book already exists (same title and author)
        for book_id, book_data in data["Books"].items():
            if (book_data["title"].lower() == book.title.lower() and 
                book_data["author"].lower() == book.author.lower()):
                print(f"Book '{book.title}' by {book.author} already exists in the library.")
                return

        new_book = {
            "title": book.title,
            "author": book.author,
            "genre": book.genre,
            "available": book.available,
        }

        data["Books"][book.id] = new_book

        with open(self.database_path,"w") as file:
            json.dump(data, file,indent=4)

        print(f"Added {book.title} by {book.author} ({book.genre}) - {book.status}")

    def checkout_book(self,query:str)->None:
        """
        Checks out a book (marks as unavailable) based on the query.

        Args:
            query (str): the query to find the book to checkout.
        """

        data = self.get_all_books()
        books_to_checkout = []

        for book_id, book_data in data["Books"].items():
            if book_data["available"] and (query.lower() in book_data["title"].lower() or query.lower() in book_data["author"].lower() or query.lower() in book_data["genre"].lower()):
                books_to_checkout.append(book_id)

        if not books_to_checkout:
            print(f"No available books found matching: '{query}'")
            return

        for book_id in books_to_checkout:
            book_title = data["Books"][book_id]["title"]
            data["Books"][book_id]["available"] = False
            print(f"Checked out: {book_title}")

        with open(self.database_path,"w") as file:
            json.dump(data, file,indent=4)

    def return_book(self,query:str)->None:
        """
        Returns a book (marks as available) based on the query.

        Args:
            query (str): the query to find the book to return.
        """

        data = self.get_all_books()
        books_to_return = []

        for book_id, book_data in data["Books"].items():
            if not book_data["available"] and (query.lower() in book_data["title"].lower() or query.lower() in book_data["author"].lower() or query.lower() in book_data["genre"].lower()):
                books_to_return.append(book_id)

        if not books_to_return:
            print(f"No checked out books found matching: '{query}'")
            return

        for book_id in books_to_return:
            book_title = data["Books"][book_id]["title"]
            data["Books"][book_id]["available"] = True
            print(f"Returned: {book_title}")

        with open(self.database_path,"w") as file:
            json.dump(data, file,indent=4)


    def get_available_books_count(self)->int:
        """
        Returns the count of available books in the library.
        """
        data = self.get_all_books()
        available_count = 0
        for book_id, book_data in data["Books"].items():
            if book_data["available"]:
                available_count += 1

        return available_count

    def clear_library(self):
        """
        Clear all the books in the library.
        """
        data = self.get_all_books()
        if len(data["Books"].items()) > 0:
            data = {"Books": {}}
            with open(self.database_path,"w") as file:
                json.dump(data, file,indent=4)
            print("The library is empty.")
        else:
            print("The library is already empty.")
