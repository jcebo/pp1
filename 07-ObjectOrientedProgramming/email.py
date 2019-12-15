from message import Message
class Email(Message):
    def __init__(self,nadawca,odbiorca,temat):
        self.nadawca=nadawca
        self.odbiorca=odbiorca
        self.temat=temat
        super().__init__()
    def send(self):
        print(f'Wysyłanie e-maila...\nOd: {self.nadawca}\nDo: {self.odbiorca}\nTemat: {self.temat}\nTreść: {self.message}')
