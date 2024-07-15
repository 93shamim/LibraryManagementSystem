from datetime import date

def view_lent_books(lent_books):
    if lent_books:    # if lent_books is not blank
        print("Lent Books are:\n")
        headers = ["SL", "Book Title", "Book Author", "ISBN", "Pub.Year", "Price", "Qnt", "Category", "Who Lent", "Borrow Date"]

        # Calculate the maximum width for each column
        col_widths = [max(len(str(item)) for item in col) for col in zip(*([headers] + 
                       [[str(index + 1), lentBook['bookTitle'], lentBook['bookAuthor'], lentBook['bookISBN'], lentBook['bookPublishingYear'],
                         lentBook['bookPrice'], lentBook['bookQuantity'], lentBook['bookCategory'], lentBook['borrowerName'], lentBook['borrowDate']] for index, lentBook in enumerate(lent_books)]))]

        # Print header row
        header_row = " | ".join(f"{header:<{col_widths[idx]}}" for idx, header in enumerate(headers))
        print(header_row)

        # Change: Calculate separator length based on column widths and spaces/separators
        separator_length = sum(col_widths) + 3 * (len(headers) - 1)
        print("-" * separator_length)

        # Print data rows with borders
        for index, lentBook in enumerate(lent_books):
            row = [
                index + 1,
                lentBook['bookTitle'],
                lentBook['bookAuthor'],
                lentBook['bookISBN'],
                lentBook['bookPublishingYear'],
                lentBook['bookPrice'],
                lentBook['bookQuantity'],
                lentBook['bookCategory'],
                lentBook['borrowerName'],
                lentBook['borrowDate']
            ]
            formatted_row = " | ".join(f"{str(item):<{col_widths[idx]}}" for idx, item in enumerate(row))
            print(formatted_row)

            # Change: Print row separator using the calculated length
            print("-" * separator_length)
    else:
        print("No books are in Lent right now.!")



# def view_lent_books(lent_books):
#     if lent_books:    # if book_list is not blank
#         print("Lent Books are:\n")
#         print("SL | Book Tile | Book Author | Book ISBN | Publishing Year | Price | Quantity | Catagory | Who Lent | Borrow Date")
#         for index, lentBook in enumerate(lent_books):
#             print(
#             index+1,
#             lentBook['bookTitle'],
#             lentBook['bookAuthor'],
#             lentBook['bookISBN'],
#             lentBook['bookPublishingYear'],
#             lentBook['bookPrice'],
#             lentBook['bookQuantity'],
#             lentBook['bookCatagory'],
#             lentBook['borrowerName'],
#             lentBook['borrowDate'],

#             sep = " , ",
#             )
#     else:
#         print("No books are in Lent right now.!")