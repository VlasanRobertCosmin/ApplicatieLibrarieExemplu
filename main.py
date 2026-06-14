from dataclasses import dataclass

#@dataclass ne ajuta sa cream mai usor o clasa simpla
# nu mai trebuie sa sa scriem manual constructorul __init__
@dataclass
class Book:
    #fiecare carte are un id unic
    id: int 
    #titlul cartii
    title: str
    #autorul carti
    author: str
    #anul 
    year: int
    #daca cartea e disponibila
    #true e disponibila 
    #false e indisponibila 
    available: bool =True
    #functie prin care imprumutam o carte 
    def borrow(self):
        self.available = False
    #metoda pentru returnanra carti
    def return_book(self):
        self.available = True
    #convertim obiectul carte intrun dictonar 
    #avem nevoie de asta ca sa putem sa salvam cartea in JSON
    def to_dict(self):
        return{
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "available": self.available
        }
    
    #METODA STATICA pentru a crea un obiect carte dintr-un dictionar
    #o folosim cand citim datele din fisierl JSON
    @staticmethod
    def from_dict(data):
        return Book(
            id=data["id"],
            title=data["title"],
            author=data["author"],
            year=data["year"],
            available=data["available"]

        )
    
