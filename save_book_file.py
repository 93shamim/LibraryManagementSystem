
def save_books(books_list):
    # take all the books
    with open("books.csv","wt") as file:
        for book in books_list:
            line = f"{book['bookTitle']},{book['bookAuthor']},{book['bookISBN']},{book['bookPublishingYear']},{book['bookPrice']},{book['bookQuantity']},{book['bookCategory']}\n"
            file.write(line)

   # print("\nBooks Backed up!")

    return books_list