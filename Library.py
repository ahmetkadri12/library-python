import json
import os
from Book import Book
from Member import Member

class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.load_data()

    def save_data(self):
        data = {
            "books": [{"title": b.title, "author": b.author, "is_borrowed": b.is_borrowed} for b in self.books],
            "members": [m.name for m in self.members]
        }
        with open("library_data.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def load_data(self):
        if os.path.exists("library_data.json"):
            with open("library_data.json", "r", encoding="utf-8") as f:
                data = json.load(f)
            self.books = []
            for b in data.get("books", []):
                book = Book(b.get("title", ""), b.get("author", ""))
                book.is_borrowed = b.get("is_borrowed", False)
                self.books.append(book)
            self.members = [Member(name) for name in data.get("members", [])]

    def add_book(self, book):
        self.books.append(book)
        self.save_data()
        print(f"Book '{book.title}' added.")

    def show_books(self):
        print("\n--- Library Books ---")
        if not self.books:
            print("No books.")
        for book in self.books:
            print(book)
        print("---------------------\n")

    def borrow_book(self, title, member_name):
        if not any(m.name.lower() == member_name.lower() for m in self.members):
            print("Member not found. Please add the member first.")
            return
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.is_borrowed:
                    print("Book already borrowed.")
                    return
                book.is_borrowed = True
                self.save_data()
                print(f"{member_name} borrowed '{book.title}'.")
                return
        print("Book not found.")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if not book.is_borrowed:
                    print("This book was not borrowed.")
                    return
                book.is_borrowed = False
                self.save_data()
                print(f"'{book.title}' returned.")
                return
        print("Book not found.")

    def add_member(self, member):
        if any(m.name.lower() == member.name.lower() for m in self.members):
            print("Member already exists.")
            return
        self.members.append(member)
        self.save_data()
        print(f"Member '{member.name}' added.")

    def show_members(self):
        print("\n--- Library Members ---")
        if not self.members:
            print("No members.")
        for member in self.members:
            print(member)
        print("-----------------------\n")
