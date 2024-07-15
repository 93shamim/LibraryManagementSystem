import table_for_search_book

def search_by_author(books_list):
    search_term = input("Enter Book Author Name for Search: ")

    found_search_item = False

    #print("\nSL | Book Tile | Book Author | Book ISBN | Publishing Year | Price | Quantity | Category ")
    for index, book in enumerate(books_list):
          if (search_term.lower() in book["bookAuthor"].lower()):

             found_search_item = True

             table_for_search_book.table_for_search_book(books_list,index,book)
            # print(f"{index+1}. {book['bookTitle']},{book['bookAuthor']},{book['bookISBN']},{book['bookPublishingYear']},{book['bookPrice']},{book['bookQuantity']},{book['bookCategory']}")
        
    if not found_search_item:
        print("Wrong keyword! Try Again")
        return
    
    return books_list