class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year


    def get_info(self):
         return f"\nНазвание книги: {self.title}, \nАвтор: {self.author}, \nГод издания: {self.year}\n"

knigga = Book("white kids", "P.Diddy", "2025")
print(knigga.get_info())