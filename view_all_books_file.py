import add_book_table

def view_all_books(books_list):

    if books_list:  # if books_list is not empty
        print("Your All Books are:\n")
        add_book_table.book_table(books_list)
    
    else:
        print("The library doesn't have any books right now.!")

# def view_all_books(books_list):
#     if books_list:    # if book_list is not blank
#         print("Your All Books are:\n")
#         print("SL | Book Tile | Book Author | Book ISBN | Publishing Year | Price | Quantity | Catagory ")
#         for index, book in enumerate(books_list):
#             print(
#             index+1,
#             book['bookTitle'],
#             book['bookAuthor'],
#             book['bookISBN'],
#             book['bookPublishingYear'],
#             book['bookPrice'],
#             book['bookQuantity'],
#             book['bookCatagory'],
#             sep = " , ",
#             )
#     else:
#         print("The library doesn't have any books right now.!")