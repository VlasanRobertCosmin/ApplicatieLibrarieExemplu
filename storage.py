#importam modulul json pentru a lucra cu fisere JSON
import json
#import pentru a verifcva si crea fisere/foldere 
import os
#importam clasa book din fiserul models.py
from models import Book


#clasa asta se ocupa de salvarea si citirea datelor
class LibraryStorage:
    def __init__(self,file_path="data/books.json"):
        self.file_path = file_path

        #verificam daca folderul data exista daca nu il creem 
        os.makedirs(os.path.dirname(file_path),exist_ok=True)

    #functie carer incarca lista de carti din fisierul JSON
    def load_books(self):
        #daca fisierul nu exista returnam o lista goala
        if not os.path.exists(self.file_path):
            return []
        

        try:
            #deschidme fisierul
            #functia open are ca parametri calea unde se afla fisierul , r sau w in functie de ce vrem sa facem
            #daca vrem sa scriem puenm "w" sau "r" daca vrem sa citim si encodingul sa fie utf-8(ultimul parametru)
            with open(self.file_path, "r",encoding="utf-8") as file:
                #citim datele
                data = json.load(file)
                #transforemama fiecare dictiona din JSON intrun obiect Book
                return [Book.from_dict(item) for item in data]
        #daca fisierul exista dar este gol sau stricat
        #returnam o lista goala in loc sa crape programul    
        except json.JSONDecodeError:
            return []
    def save_book(self,books):
        #transformam fiecare obiect in dictionar pentru al putea salva in JSON 
        data = [book.to_dict() for book in books]
        #deschidem fisierul pentru a putea scrie
        with open(self.file_path,"w",encoding="utg-8") as file:
            #salvam datele in format JSON
            #facem o identare de 4 ca sa fie fiserul mai lizibil 
            #ensure_ascii = false permite folosirea caracteelor romanesti
            json.dump(data,file,indent = 4,ensure_ascii=False)
