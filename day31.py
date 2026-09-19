# DAY 30: OOP Project - Library Management System
# Features:
# 	0. Simple menu
# 	1. Add books
# 	2. Display books
# 	3. Borrow a book
# 	4. Return a book

class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True
    def display(self):
            print(f"ID: {self.book_id}")
            print(f"Title: {self.title}")
            print(f"Author: {self.author}")
            status = "Available" if self.available==True else "Borrowed"
            print(f"Status: {status}")
            print("-" * 30)
class Library:
    def __init__(self):
        self.books = []
    def add_book(self):
        id = input("Enter Book Id: ")
        for book in self.books:
            if id == book.book_id:
                print('Book Id already taken, please enter a different id')
                return
        title = input("Enter Book Title: ")
        author = input("Enter Author: ")
        book = Book(id, title, author)
        self.books.append(book)
        print("Book added successfully!")
    def display_books(self):
        if len(self.books)==0:
            print("No books available.")
            return
        print("\n--- Library Books ---")
        for book in self.books:
            book.display()
    def borrow_book(self):
        book_id = input("Enter Book ID to borrow: ")
        for book in self.books:
            if book.book_id == book_id:
                if book.available==True:
                    book.available = False
                    print("Book borrowed successfully!")
                else:
                    print("Book is already borrowed.")
                return
        print("Book not found.")
    def return_book(self):
        book_id = input("Enter Book ID to return: ")
        for book in self.books:
            if book.book_id == book_id:
                if book.available==False:
                    book.available = True
                    print("Book returned successfully!")
                else:
                    print("Book is already available.")
                return
        print("Book not found.")
    def delete_book(self):
        book_id = input("Enter Bokk ID to delete: ")
        for book in self.books:
            if book.book_id == book_id:
                confirm = input("Press y to confirm: ")
                self.books.remove(book) 
                print("Book deleted successfully")
                return 
        print("Book not found.")
        
# Create Library object
library = Library()
# Menu
while True:
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Delete Book")
    print("6. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        library.add_book()
    elif choice == "2":
        library.display_books()
    elif choice == "3":
        library.borrow_book()
    elif choice == "4":
        library.return_book()
    elif choice == "5":
        library.delete_book()
    elif choice == "6":
        print("Thank you!")
        break
    else:
        print("Invalid choice.")
