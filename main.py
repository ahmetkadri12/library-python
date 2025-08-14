from Library import Library
from Book import Book
from Member import Member

def menu():
    library = Library()
    while True:
        print("\n1. Show Books")
        print("2. Add Book")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Show Members")
        print("6. Add Member")
        print("7. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            library.show_books()
        elif choice == "2":
            title = input("Book Title: ").strip()
            author = input("Author: ").strip()
            if title and author:
                library.add_book(Book(title, author))
            else:
                print("Title and author are required.")
        elif choice == "3":
            title = input("Book Title to Borrow: ").strip()
            member_name = input("Member Name: ").strip()
            library.borrow_book(title, member_name)
        elif choice == "4":
            title = input("Book Title to Return: ").strip()
            library.return_book(title)
        elif choice == "5":
            library.show_members()
        elif choice == "6":
            name = input("Member Name: ").strip()
            if name:
                library.add_member(Member(name))
            else:
                print("Name is required.")
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    menu()
