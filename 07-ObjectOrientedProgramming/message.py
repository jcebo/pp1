class Message():
    def __init__(self):
        self.message=''
    def set_message(self,message):
        message=message.lower()
        message=message.capitalize()
        message=message+(' Bye.')
        self.message=message
        