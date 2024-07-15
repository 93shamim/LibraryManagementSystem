
def table_for_search_book(books_list,index,book):
             
            #Table Area start
             headers = ["SL", "Book Title", "Book Author", "ISBN", "Pub.Year", "Price", "Qnt", "Category"]
            
             # Calculate the maximum width for each column
             col_widths = [max(len(str(item)) for item in col) for col in zip(*([headers] + 
                        [[str(index + 1), book['bookTitle'], book['bookAuthor'], book['bookISBN'], book['bookPublishingYear'],
                            book['bookPrice'], book['bookQuantity'], book['bookCategory']] for index, book in enumerate(books_list)]))]

             # Print header row
             header_row = " | ".join(f"{header:<{col_widths[idx]}}" for idx, header in enumerate(headers))
             print(header_row)

             # Change: Calculate separator length based on column widths and spaces/separators
             separator_length = sum(col_widths) + 3 * (len(headers) - 1)
             print("-" * separator_length)

             #print("\nSL | Book Tile | Book Author | Book ISBN | Publishing Year | Price | Quantity | Category ")
             #row = (f"{index+1}. {book['bookTitle']},{book['bookAuthor']},{book['bookISBN']},{book['bookPublishingYear']},{book['bookPrice']},{book['bookQuantity']},{book['bookCategory']}")
            
             row = [
                    str(index + 1),
                    book['bookTitle'],
                    book['bookAuthor'],
                    book['bookISBN'],
                    book['bookPublishingYear'],
                    book['bookPrice'],
                    book['bookQuantity'],
                    book['bookCategory']
                ]

             formatted_row = " | ".join(f"{str(item):<{col_widths[idx]}}" for idx, item in enumerate(row))
             print(formatted_row)

             # Change: Print row separator using the calculated length
             print("-" * separator_length)
             #Table Area End