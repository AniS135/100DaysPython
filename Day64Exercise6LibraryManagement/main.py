'''
Write a Library class with no_of_books and books 
as two instance variables. Write a program to create 
a library from this Library class and show how you 
can print all books, add a book and get the number of 
books using different methods. Show that your program 
doesnt persist the books after the program is stopped!
'''

class Library:
    def __init__(self) -> None:
        self.num_of_books = 0
        self.books = []
    
    def add(self, book):
        self.books.append(book)
        self.num_of_books += 1
    
    def isSame(self):
        return len(self.books) == self.num_of_books

library1 = Library()
library2 = Library()
library3 = Library()

library1.add("Harry Potter")
library2.add("Harry Potter")
library3.add("Harry Potter")

library2.add("World Record")
library3.add("World Record")

library3.add("2 States")

print(library1.isSame(), library1.num_of_books)
print(library2.isSame(), library2.num_of_books)
print(library3.isSame(), library3.num_of_books)
