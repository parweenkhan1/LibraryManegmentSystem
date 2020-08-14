class Library:
    def __init__(self,list_of_books,library_name):
        # creating dictionary for all the books in the library
        self.lend_data = {}
        self.list_of_books = list_of_books
        self.library_name = library_name
        # adding books into the library
        for books in self.list_of_books:
            # None lend this book
            self.lend_data[books] = None


    #for displaying the books present in the library
    def display_books(self):
        for index,books in enumerate(self.list_of_books):
            print(f"{index}:{books}")

    def lend_book(self,book,lender):
        if book in self.list_of_books:
            if self.lend_data[book] is None:
                self.lend_data[book] = lender
            else:
                print(f"Sorry but this book is lend by {self.lend_data[book]}")
        else:
            print(f"sorry u have written wrong book name")
    def return_book(self,book,lender):
        if book in self.list_of_books:
            if self.lend_data[book] is not None:
                self.lend_data.pop(book)
            else:
                print("sorry the book is not lend")
        else:
            print("You enter the wrong name of the book")
    def add_book(self,book):
        self.list_of_books.append(book)
        self.lend_data[book] = None
    def delet_book(self,book):
        self.list_of_books.remove(book)
        self.lend_data.pop(book)
def main():
    list_of_books = ["twilight saga","Vampire diaries","Harry potter","Robin hood","The Witch Hunter","Swasan saga","The Wonky Donkey","EMMA and the lost Unicorn","The Mermaid","Beauty and the Beast"]
    library_name = "Central library"
    secret_key = 123456

    Central_library=Library(list_of_books,library_name)
    print(f"Welcome to {Central_library.library_name} Library.")
    print("Type EXIT to exit from library.\n type ADD to add a book to library.")
    print("Type DEL to delet a book from library.")
    print("Type DISPLAY to display the book of the library.")
    print("Type LEND to lend a book.")
    Exit = False
    while Exit is not True:
        _input = input("input the service u want from our Library.")
        print("\n")

        if _input == "EXIT":
            Exit = True
        if _input == "DISPLAY":
            Central_library.display_books()

        if _input == "ADD":
            input1 = input("enter the book name")
            Central_library.add_book(input1)
        if _input == "DEL":
            input1 = int(input("enter the secret key"))
            if input1 == secret_key:
                Central_library.delet_book(input1)
            else:
                print("Sorry we can't delet this book")
        if _input == "LEND":
            input1 = input("enter the book name")
            input2 = input("enter the lender's name")
            Central_library.lend_book(input1,input2)

        if _input == "RETURN":
            input1 = input(" Which book u want to return ")

            input2 = input("enter the Lender's name")
            Central_library.return_book(input1,input2)


if __name__ =="__main__":
    main()
