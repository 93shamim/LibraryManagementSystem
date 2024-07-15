
def save_lentBooks(lent_books):
    # take all the lent books
    with open("lentbooks.csv","at") as file:
        for lentBook in lent_books:
            line = f"{lentBook['bookTitle']},{lentBook['bookAuthor']},{lentBook['bookISBN']},{lentBook['bookPublishingYear']},{lentBook['bookPrice']},{lentBook['bookQuantity']},{lentBook['bookCategory']},{lentBook['borrowerName']},{lentBook['borrowDate']}\n"
            file.write(line)

   # print("\nBooks Backed up!")

    return lent_books
