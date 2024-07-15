
def search_book_byAnything(books_list):
    search_term = input("Search book using any keywords : ")

    found_search_item = False

    print("\nSL | Book Tile | Book Author | Book ISBN | Publishing Year | Price | Quantity | Category ")
    for index, book in enumerate(books_list):
          if (search_term.lower() in book["bookTitle"].lower() or 
              search_term.lower() in book["bookAuthor"].lower() or
              search_term.lower() in book["bookISBN"].lower() or
              search_term.lower() in book["bookPublishingYear"].lower() or
              search_term.lower() in book["bookPrice"].lower() or
              search_term.lower() in book["bookQuantity"].lower() or
              search_term.lower() in book["bookCategory"].lower()):

             found_search_item = True
             print(f"{index+1}. {book['bookTitle']} , {book['bookAuthor']} , {book['bookISBN']} , {book['bookPublishingYear']} , {book['bookPrice']} , {book['bookQuantity']} , {book['bookCategory']}")
        
    if not found_search_item:
        print("Wrong keyword! Try Again")
        return
    
    return books_list