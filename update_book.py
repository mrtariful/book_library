from save_all_books import save_all_books
def update_book(all_books):
    if not all_books:
        print("No books available to update")
        return all_books
    isbn_to_update=input("Enter the ISBN of the book to update")
    for book in all_books:
        if str(book["isbn"]) == isbn_to_update:
            print(f"Found book:{book}")
            book["title"] = input("Enter new title:")
            book["author"] = input("Enter the author:")
            book["price"] = input("Enter the new price:")
            book["quantity"] = input("Enter quantity:")
            print("Book update succesfully")
            save_all_books(all_books)
            
            