
import search_book_byAnything_file
import save_book_file

def delete_book(books_list):
    print("You are going to Delete a Book: ")

    # 1. Search Book
    search_book_byAnything_file.search_book_byAnything(books_list)

    # 2. Select from search result by index
    select_index = (int(input("Enter index of Book for Delete: ")) -1)

    # 3. Delete from list using input index
    books_list.pop(select_index)
    
    # auto save or backup to .csv file
    save_book_file.save_books(books_list)

    print("\nBook Deleted Successfully!")

    return books_list
