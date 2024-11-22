def view_all_books(all_books):
    if all_books != []:
        for book in all_books:
            print(f"Title : {book["title"]} | Author : {book["author"]} | Isbn : {book["isbn"]} | Year : {book["year"]} | price : {book["price"]} | Quantity : {book["quantity"]}")
        else:
            print("No book found in all_book")