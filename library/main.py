from library.book import Book
from library.library_system import LibrarySystem

if __name__ == "__main__":
    # the main database for the library to pass to the class
    database = "./database.json"
    my_library = LibrarySystem(database)

    #search for a book
    print("Searching Book...")
    result = my_library.search_books("gatsby")
    print("---------------------------------------")

    #get the total amount of books in the library
    print("Total books in the current library:")
    total_book_count = my_library.get_total_books_count()
    print(f"Total books: {total_book_count}")

    print("----------------------------------------")

    #Create a book object so it can be added to the library
    print("Adding books to the library...")
    print("----------------------------------------")
    book1 = Book("1984","George Orwell","dystopian fiction")
    my_library.add_book_to_library(book1)
    book2 = Book("Pride and Prejudice","Jane Austen","romance")
    my_library.add_book_to_library(book2)

    # Get all the books in the library
    print("----------------------------------------")
    print("Getting all the books in the library:")
    print("----------------------------------------")
    my_library.get_all_books(verbose=1)

    print("----------------------------------------")

    #checkout a book
    print("Checking out books from the library...")
    print("---------------------------------------")
    my_library.checkout_book("1984")
    print("\n")

    # Get all the books in the library
    print("----------------------------------------")
    print("Getting all the books in the library:")
    print("----------------------------------------")
    my_library.get_all_books(verbose=1)

    print("----------------------------------------")
    
    # Return a book
    print("Returning a book to the library...")
    print("----------------------------------------")
    my_library.return_book("1984")
    print("----------------------------------------")

    print("All the current books in the library:")
    my_library.get_all_books(verbose=1)
    print("----------------------------------------")

    print("Available books count:")
    available_count = my_library.get_available_books_count()
    print(f"Available books: {available_count}")