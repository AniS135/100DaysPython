class Library:
    def __init__(self) -> None:
        self.noBooks = 0
        self.books = []
    
    def addBooks(self, book):
        self.books.append(book)
        self.noBooks = len(self.books)

    def showInfo(self):
        print(f"The library has {self.noBooks} books. The books are")

        for book in self.books:
            print(book)
    


l1 = Library()
l1.addBooks("Harry Potter1")
l1.addBooks("Harry Potter2")
l1.addBooks("Harry Potter3")
l1.addBooks("Harry Potter4")
l1.showInfo()
