def remove_book(all_books):
    if not all_books:
        print("No book found")
        return
    isbn_for_remove=int(input("Enter your isbn numberr for remove:"))
    for book in all_books:
        if book.get("isbn") == isbn_for_remove:
            all_books.remove(book)
            print("Book removed succesfully")
            return
        