class ebook():
    def __init__(self):
        self.title=''
        self.author=''
        self.pages=0
        self.isopen=False
        self.actual_page=0
    def set_title(self,new_title):
        self.title=new_title
    def set_author(self,new_author):
        self.author=new_author
    def set_pages(self,new_pages):
        self.pages=new_pages
    def open_book(self):
        self.isopen=True
    def close_book(self):
        self.isopen=False
    def show_status(self):
        if self.isopen==False:
            print("Ksiązka jest zamknięta")
        else:
            print(f'Tytul ksiazki: {self.title}, autor: {self.author}, liczba stron: {self.pages}, biezaca strona: {self.actual_page}')        
    def read_page(self):
        if self.isopen==False:
            print("Ksiązka jest zamknięta")

        