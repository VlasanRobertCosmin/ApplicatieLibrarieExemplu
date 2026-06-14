#importam clasa book pentru a putea crea obiecte de tip carte
from book import Book
#creem o clasa care continelogica principala a aplicatiei 
#aici se fac operatiile :adaugare, cautare,returnare, stergere
class LibraryServices:
    def __init__(self,storage):
        self.storage = storage

        #in momentul in care pornim aplicata incarcam cartile slavate anterior in Json
        self.books = self.storage.load_books()

    #creem o metoda care calculeaza urmatorul ID disponibil pentru o carte noua
    def get_next_id(self):
        #daca nu exista nico care primul ID va fi 1
        if not self.books:
            return 1
    #daca exista carti , luam cel mai mare ID si adaugam 1 
        return max(book.id for book in self.books) + 1
    def add_book(self,title,author,year):
         #creem un obiect nou 
        book = Book(
                id=self.get_next_id(),
                title=title,
                author=author,
                year=year
        )

        #adaugam cartea in lista de carti
        self.books.append(book)
        #salvam lista actualizata in fiseul JSON
        self.storage.save_books(self.books)
    #metoda care returneaza toate cartile din biblioteca
    def get_all_books(self):
        return self.books
    #metoda care cauta o carte dupa titlu 
    def get_title(self,title):
        results = []
        #parcurgem lista de carti si adaugam in rezultate cartile care contin titlul cautat
        for book in self.books:
            #cautarea nu tine cont de litere mari sau mici 
            #exemplu :ion sau ION 
            if title.lower() in book.title.lower():
                results.append(book)
        return results         
    #metoda pentru a imprumuta o carte 
    def borrow_book(self,book_id):
        #cautam cartea dupa ID
        for book in self.books:
            if book.id == book_id:
                #verificam daca e available 
                if book.available:

                    #salvam modificarea in fisier
                    self.storage.save_books(self.books)
                    return  "Cartea a fost imprumutata cu succes."
            else:
                return "Cartea nu este disponibila pentru imprumut."
        return "Cartea cu ID-ul specificat nu a fost gasita."
    #metoda pentru returnarea carti 
    def return_book(self,book_id):
        #cautam cartea dupa ID
        for book in self.books:
            if book.id == book_id:
                #verificam daca e imprumutata 
                if not book.available:
                    book.return_book()
                    #salvam modificarea in fisier
                    self.storage.save_books(self.books)
                    return "Cartea a fost returnata cu succes."
                else:
                    return "Cartea nu a fost imprumutata."
        return "Cartea cu ID-ul specificat nu a fost gasita."
    #metoda pentru stergerea unei carti
    def delete_book(self,book_id):
        #cautam cartea dupa ID
        for book in self.books:
            if book.id == book_id:
                self.books.remove(book)
                #salvam modificarea in fisier
                self.storage.save_books(self.books)
                return "Cartea a fost stearsa cu succes."
        return "Cartea cu ID-ul specificat nu a fost gasita."
    