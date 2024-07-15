import search_book_byAnything_file
import save_lent_book_file
#import view_lent_books_file
#import os
#import restore_books_file
from datetime import date
import add_book_table

lent_books = []

def lend_book(books_list):
    #print("You are going to lend a Book !")

    #  1. Show Available Book for lent
    if books_list:    # if book_list is not blank
        print("Here are the Available Books for lent:\n")
        add_book_table.book_table(books_list)
        
        # print("SL | Book Tile | Book Author | Book ISBN | Publishing Year | Price | Quantity | Catagory ")
        # for index, book in enumerate(books_list):
        #     print(
        #         index+1,
        #         book['bookTitle'],
        #         book['bookAuthor'],
        #         book['bookISBN'],
        #         book['bookPublishingYear'],
        #         book['bookPrice'],
        #         book['bookQuantity'],
        #         book['bookCatagory'],
        #         sep = " , ",
        #     )
    else:
        print("No Available Books for lent !")
    

    # # 1. Search book
    # search_book_byAnything_file.search_book_byAnything(books_list)

    # 2. Input index number for select book
    select_index = (int(input("\nEnter Index number of Book for Lent: "))-1)

    # 3. Add the selected book to lent_books list
    selected_book = books_list[select_index].copy()

    # 4. input quantity & Set bookQuantity for the selected book
    lentQuanitiy = int(input("Enter Book Quantity for Lent: "))
    selected_book["bookQuantity"]= lentQuanitiy

    # 5. Set bookQuantity for the selected book
    

    #lent_books[-1]['bookQuantity'] = lentQuanitiy

    # 6. input who want to lent
    borrowerName = input("Enter borrower's Name: ")
    selected_book["borrowerName"] = borrowerName

     # 6. Pick lent date
    borrowDate = date.today()
    selected_book["borrowDate"] = borrowDate

    #append above key:valu with selected_book
    lent_books.append(selected_book)

    # auto save or backup to .csv file
    save_lent_book_file.save_lentBooks(lent_books)   

    print(f"\nBook '{lent_books[-1]['bookTitle']}' is lent Sucessfully")

    #view_lent_books_file.view_lent_books(lent_books)

    return lent_books