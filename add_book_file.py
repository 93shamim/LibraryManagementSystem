import save_book_file

def add_book(books_list):
    print("You are going add new Book:")

    bookTitle = input("Enter Book Title: ")
    bookAuthor = input("Enter Book Author: ")
    bookISBN = input("Enter Book ISBN: ")
    bookPublishingYear = input("Enter Book Publishing Year: ")
    bookPrice = input("Enter Book Price: ")
    bookQuantity = int(input("Enter Book Quantity: "))
    bookCategory = input("Enter Book Category: ")

    book = {
        "bookTitle": bookTitle,
        "bookAuthor": bookAuthor,
        "bookISBN": bookISBN,     
        "bookPublishingYear": bookPublishingYear,     
        "bookPrice": bookPrice,     
        "bookQuantity": bookQuantity,     
        "bookCategory": bookCategory,     
        }
    
    books_list.append(book)
    
    # auto save or backup to .csv file
    save_book_file.save_books(books_list)

    print("\nBook added Sucessfully!")

    return books_list


