class TV():
    def __init__(self):
        self.is_on=False
    def on(self):
        self.is_on=True
    def off(self):
        self.is_on=False
    def show_status(self):
        if self.is_on==False:
            print( 'Telewizor jest wyłączony')
        else:
            print ('Telewizor jest załączony')
        
tv=TV()
tv.show_status()
tv.on()
tv.show_status()
tv.off()
tv.show_status()
