

def restore_books(books_list):
    with open("books.csv","r") as file:
        for line in file.readlines():
            line_splitted = line.strip().split(",")
            book = {
                "bookTitle":            line_splitted[0],
                "bookAuthor":           line_splitted[1],
                "bookISBN":             line_splitted[2],    
                "bookPublishingYear":   line_splitted[3],      
                "bookPrice":            line_splitted[4],     
                "bookQuantity":         line_splitted[5],     
                "bookCategory":         line_splitted[6],    
            }
            books_list.append(book)
        # print("Books Restored Sucessfully!")

        return books_list