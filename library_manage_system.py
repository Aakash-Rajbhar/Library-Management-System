#Implement a student library system using oops where student can borrow a book from the list of books.
#Create a seperate library & student class. Your program must be menu driver.You are free to choose methods and atributes of your choice to implement the functionality.

class Library:
    def __init__(self, listofBooks):
        self.books = listofBooks     #This is for displaying the Books
    
    def displayAvailableBooks(self):
        print("Books present in the Library are : ")
        for book in self.books:
            print("* "+book)

    def borrowBook(self,bookName):
        if bookName in self.books:
            print(f"You have been isued {bookName}. Please keep it safe and return it within 30 days.")
            self.books.remove(bookName)
            return True

    def returnBook(self, bookName):
        self.books.append(bookName)
        print("Thanx for returning this book I hope you enjoyed it. Have a great day Ahead!!")

#----------------------Student------------------------------------------------------

class Student:
    def requestBook(self):
        self.book = input("Enter the name of book you want to borrow : ")
        return self.book

    def returnBook(self):
        self.book = input("Enter the name of the book you want to return : ")
        return self.book

if __name__ == "__main__" :
    centralLibrary = Library(["Jungle Book", "Arabian Nights", "Avengers", "Honeycomb", "Inception", "Matrix", "King Kong", "Vistas", "Flamingo", "RD Sharma"])

student = Student()

while (True):
    try:

        Wlcm_msg = "************************ WELCOME TO THE CENTRAL LIBRARY **************************\n* Please Choose an option\n1. Show the List of books.\n2. Request for a book.\n3. Add/Return a book.\n4. Exit"

        print(Wlcm_msg)
        a = int(input("Enter a choice : "))
        if a == 1:
            centralLibrary.displayAvailableBooks()

        elif a == 2 :
            centralLibrary.borrowBook(student.requestBook())

        elif a == 3 :
            centralLibrary.returnBook(student.returnBook())

        elif a == 4 :
            print("Thanx for coming to the CENTRAL LIBRARY....")
            exit()
    
        else :
            print("Invalid Choice.")

    except :
        print("Sorry Something wrong")