
def restore_lentbooks(lent_books):
    with open("lentbooks.csv","r") as file:
        for line in file.readlines():
            line_splitted = line.strip().split(",")
            lentbook = {
                "bookTitle":            line_splitted[0],
                "bookAuthor":           line_splitted[1],
                "bookISBN":             line_splitted[2],    
                "bookPublishingYear":   line_splitted[3],      
                "bookPrice":            line_splitted[4],     
                "bookQuantity":         line_splitted[5],     
                "bookCategory":         line_splitted[6],    
                "borrowerName":         line_splitted[7],    
                "borrowDate":           line_splitted[8],    
            }
            lent_books.append(lentbook)
        # print("Books Restored Sucessfully!")

        return lent_books