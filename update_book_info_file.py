#import search_book_byAnything_file
import save_book_file
import add_book_table

def update_book_info(books_list):
    print("You are going to Update Book info:\n")

    # 1. Search Book
    #search_book_byAnything_file.search_book_byAnything(books_list)

    if books_list:    # if book_list is not blank
        print("Here are the Available Books for Update:\n")
        add_book_table.book_table(books_list)
    else:
        print("No Available Books for Update !")

    # 2. Select from search result by index
    select_index = (int(input("Enter index of Book for update: ")) -1)

    # print(books_list[select_index])
  
    # 3. new input for update
    new_bookTitle = input(f"Enter New Title for Book-{select_index+1}: ")
    new_bookAuthor = input(f"Enter New Author Name for Book-{select_index+1}: ")
    new_bookISBN = input(f"Enter New ISBN for Book-{select_index+1}: ")
    new_bookPublishingYear = input(f"Enter New Publishing Year for Book-{select_index+1}: ")
    new_bookPrice = input(f"Enter New Price for Book-{select_index+1}: ")
    new_bookQuantity = input(f"Enter New Quantity for Book-{select_index+1}: ")
    new_bookCategory = input(f"Enter New Category for Book-{select_index+1}: ")

    # 4. update or replace to books_list
    books_list[select_index].update(
            {
                "bookTitle": new_bookTitle,
                "bookAuthor": new_bookAuthor,
                "bookISBN": new_bookISBN,     
                "bookPublishingYear": new_bookPublishingYear,     
                "bookPrice": new_bookPrice,     
                "bookQuantity": new_bookQuantity,     
                "bookCategory": new_bookCategory, 
            }
        )
    
    # auto save or backup to .csv file
    save_book_file.save_books(books_list)

    print(f"\nBook-{select_index+1} Updated Successfully!")

    return books_list
