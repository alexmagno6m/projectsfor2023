class Library():
    loan = 0
    consults = 0
    book_numbers = 0
    copies = 0

    def __init__(self, title, author, pages, genre):
        self.title = title
        self.author = author
        self.pages = pages
        self.genre = genre
        self.copies += 1
        Library.book_numbers += 1

    def set_loan(self):
        self.loan += 1

    def set_consults(self):
        self.consults += 1

    def __del__(self):
        Library.book_numbers -= 1
        if self.copies >= 1:
            self.copies -= 1
        else:
            return "there are no more copies"

    def new_copies(self):
        self.copies += 1
        Library.book_numbers += 1

    @property
    def book_status(self):
        return '''the book has been:
        lent {} times,
        consulted {} times, and
        there are {} copies in total \
        '''.format(self.loan, self.consults, self.copies)

    def __repr__(self):
        #       return "Library {} {} {} {}".format(self.title, self.author, self.pages, self.genre)
        #       return f'Library({self.title}, {self.author}, {self.pages}, {self.genre})'
        #       la salida es engañosa porque la clase heredada no pertenece a la clase library
        #       solution
        return f'{type(self).__name__}({self.title}, {self.author}, {self.pages}, {self.genre})'

book1 = Library("Crimen y castigo",
                "Dostoevsky",
                420,
                "thriller")
book2 = Library("La melancolia de los feos",
                "Mario Mendoza",
                415,
                "Suspense")

book2.new_copies()
book2.set_consults()

print(book2.book_status)
print(book2)


class SchoolLibrary(Library):
    def __init__(self, title, author, pages, genre, level):
        super().__init__(title, author, pages, genre)
        self.level = level

    # static method
    @staticmethod
    def value(price, cost):
        return price - cost

    @staticmethod
    def set_book_number(number):
        SchoolLibrary.book_numbers = number





book3 = SchoolLibrary("Math 11",
                      "Education Secretary",
                      340,
                      "Educational",
                      "High School")
book3.set_consults()
print(book3.book_status)

print(book3)
# Check class
print(type(book3))
# Check class instance
print(isinstance(book3, Library))
# Chech SchoolLibrary instances
print(book3.book_numbers)
# Method static uses
print(SchoolLibrary.value(500, 400))
SchoolLibrary.set_book_number(6)
print(SchoolLibrary.book_numbers)