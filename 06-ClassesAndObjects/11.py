class TV():
    def __init__(self):
        self.is_on=False
        self.channel_no=1
    def on(self):
        self.is_on=True
    def off(self):
        self.is_on=False
    def show_status(self):
        if self.is_on==False:
            print( 'Telewizor jest wyłączony')
        else:
            print (f'Telewizor jest załączony, kanał {self.channel_no}')
        
tv=TV()
tv.show_status()
tv.on()
tv.show_status()
tv.off()
tv.show_status()
