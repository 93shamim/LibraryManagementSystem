import table_for_search_book

def search_by_title_isbn(books_list):
    search_term = input("Enter Book Title or ISBN for Search: ")

    found_search_item = False

    for index, book in enumerate(books_list):
          if (search_term.lower() in book["bookTitle"].lower() or 
              search_term.lower() in book["bookISBN"].lower()):

             found_search_item = True

             table_for_search_book.table_for_search_book(books_list,index,book)

    if not found_search_item:
        print("Wrong keyword! Try Again")
        return
    
    return books_list