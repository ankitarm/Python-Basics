# library class
# methods to display books
# method for customer lending
# add book function to donate book
# return book function
# dict-book:person
# who owns book if not present


# harryLibrary = library(listofbooks, library_name) #constructor

# create a main function and run an infinite while loop asking for input
# display books
# display available books
# lend books
# return book
dictoptions={1:"Display all books",2:"Lend a book",3:"Add a book",4:"Return book"}

class Library:

    def __init__(self, listofbooks, libname):
        self.listofbooks = listofbooks
        self.libname = libname
        self.LendDict = {}

    def display_all_books(self):
        print(f" Displaying the books in library {self.libname} ")
        for books in self.listofbooks:
            print(books, end="  ")

    def lendbook(self, user, book):
        if book not in self.LendDict.keys():
            self.LendDict.update({book:user})
            print("Thanks for lending. Database updated.")
        else:
            print("Sorry the book is taken by "+self.LendDict[book])

    def addbook(self, book):
        self.listofbooks.append(book)
        print("Thanks for Adding. Database updated.")

    def returnbook(self, book):
        self.LendDict.pop(book)
        print("Thanks for Returning. Database updated.")

if __name__ == '__main__':

    l = Library(["book1", "book2", "book3", "book4", "book5", "book6", "book7", "book8", "book9", "book10"],
                "Mylibrary")

    while True:
        print("Hey There!!!!!!\nWelcome to the Library\nHow can I help you.....\n")
        for key, value in dictoptions.items():
            print(f"{key}.{value}", end="  ")
        input_from_user = int(input("\nEnter :"))

        if input_from_user == 1:
           l.display_all_books()

        elif input_from_user == 2:
            book = (input("Enter book name: "))
            user = (input("Enter your name: "))
            l.lendbook( user, book)

        elif input_from_user == 3:
            book = (input("Enter book name to add to library: "))
            l.addbook(book)


        elif input_from_user == 4:
            book = (input("Enter book name to add to library: "))
            l.returnbook(book)
        else:
            print("Invalid Input")

        print("\nPress c to continue and q to quit.")
        cq_input=""
        while (cq_input!="c" or cq_input!="q"):
            cq_input = input()
            if cq_input=="q":
                exit()
            elif cq_input=="c":
                break
            else:
                pass

