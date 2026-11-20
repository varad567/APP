"""
Experiment 01 - Library Management System using OOP (CO-1)
Manages books and patrons: add books, register patrons, borrow and return books.
"""


class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_available = True

    def __str__(self):
        status = "Available" if self.is_available else "Borrowed"
        return f"[{self.book_id}] {self.title} by {self.author} - {status}"


class Patron:
    def __init__(self, patron_id, name):
        self.patron_id = patron_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        titles = [b.title for b in self.borrowed_books]
        return f"[{self.patron_id}] {self.name} - Borrowed: {titles if titles else 'None'}"


class Library:
    def __init__(self, name):
        self.name = name
        self.books = {}
        self.patrons = {}

    def add_book(self, book):
        self.books[book.book_id] = book
        print(f"Book added: {book.title}")

    def register_patron(self, patron):
        self.patrons[patron.patron_id] = patron
        print(f"Patron registered: {patron.name}")

    def borrow_book(self, patron_id, book_id):
        patron = self.patrons.get(patron_id)
        book = self.books.get(book_id)
        if patron is None or book is None:
            print("Invalid patron ID or book ID.")
            return
        if not book.is_available:
            print(f"Sorry, '{book.title}' is already borrowed.")
            return
        book.is_available = False
        patron.borrowed_books.append(book)
        print(f"{patron.name} borrowed '{book.title}'.")

    def return_book(self, patron_id, book_id):
        patron = self.patrons.get(patron_id)
        book = self.books.get(book_id)
        if patron is None or book is None or book not in patron.borrowed_books:
            print("This book was not borrowed by this patron.")
            return
        book.is_available = True
        patron.borrowed_books.remove(book)
        print(f"{patron.name} returned '{book.title}'.")

    def display_books(self):
        print(f"\n--- Books in {self.name} ---")
        for book in self.books.values():
            print(book)

    def display_patrons(self):
        print(f"\n--- Patrons of {self.name} ---")
        for patron in self.patrons.values():
            print(patron)


if __name__ == "__main__":
    library = Library("City Library")

    library.add_book(Book(101, "Python Crash Course", "Eric Matthes"))
    library.add_book(Book(102, "Clean Code", "Robert C. Martin"))
    library.add_book(Book(103, "Introduction to Algorithms", "Cormen"))

    library.register_patron(Patron(1, "Varad"))
    library.register_patron(Patron(2, "Ansh"))

    print()
    library.borrow_book(1, 101)
    library.borrow_book(2, 101)   # already borrowed
    library.borrow_book(2, 103)

    library.display_books()
    library.display_patrons()

    print()
    library.return_book(1, 101)
    library.display_books()
