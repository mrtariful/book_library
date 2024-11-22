from remove_book import remove_book
from update_book import update_book
import add_books
import view_all_books
all_books=[]
while True:
    print("Welcome to Library Management System")
    print("0.Exit")
    print("1.Add Books")
    print("2.View all Books")
    print("3.Update Book")
    print("4.Remove book")

    menu=input("Select any number:")

    if menu == "0":
        print("Thanks for using Library Management System")
        break
    elif menu == "1":
        all_books=add_books.add_books(all_books)
    elif menu == "2":
        view_all_books.view_all_books(all_books)
    elif menu == "3":
        update_book(all_books)
    elif menu == "4":
        remove_book(all_books)
    else:
        print("Choose a valid number")
        
        
