import add_book_file
import save_book_file
import view_all_books_file
import restore_books_file
import search_Title_isbn_file
import search_by_author_file
import update_book_info_file
import delete_book_file
import lend_book_file
import view_lent_books_file
import restore_lent_books_file
from lend_book_file import lent_books
import os
import remaining_book_qnt

books_list = []

#lent_books = []

if os.path.exists("books.csv"):
    restore_books_file.restore_books(books_list)


if os.path.exists("lentbooks.csv"):
    restore_lent_books_file.restore_lentbooks(lent_books)
else:
    pass


menu_text = """
1. Add Books
2. View All Books
3. Search Book by Title Or ISBN
4. Search Book by Author
5. Delete Book
6. Lend Book
7. View Lent Books
8. Return book
9. Update
10. Remaingin
0. Exit
"""

print("\n*** Welcome to Library Management System ***")

while True:
    
    print("\nYour Options!")
    print(menu_text)
    choice = input("Enter Your Choice: ")

    if choice == "1":
       books_list = add_book_file.add_book(books_list)
    elif choice == "2":
        view_all_books_file.view_all_books(books_list)
    elif choice == "3":
        search_Title_isbn_file.search_by_title_isbn(books_list)
    elif choice == "4":
        search_by_author_file.search_by_author(books_list)
    elif choice == "5":
        delete_book_file.delete_book(books_list)
    elif choice == "6":
        lend_book_file.lend_book(books_list)
    elif choice == "7":
        view_lent_books_file.view_lent_books(lent_books)


    elif choice == "9":
        update_book_info_file.update_book_info(books_list)
    elif choice == "10":
        remaining_book_qnt.remaining_qnt(books_list)

    # elif choice == "10":
    #     save_book_file.save_books(books_list)

    elif choice == "0":
        break
    else:
        print("Wrong choice!")
