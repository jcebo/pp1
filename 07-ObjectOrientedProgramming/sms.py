from message import Message
class Sms(Message):
    def __init__(self,nr_nadawcy,nr_odbiorcy):
        self.nr_nadawcy=nr_nadawcy
        self.nr_odbiorcy=nr_odbiorcy
        super().__init__()
    def send(self):
        print (f'Wysyłanie wiadomości sms...\nOd: {self.nr_nadawcy}\nDo: {self.nr_odbiorcy}\nTreść: {self.message}')
        
