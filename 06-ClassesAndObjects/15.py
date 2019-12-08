class TV():
    def __init__(self):
        self.is_on=False
        self.channel_no=1
        self.channels_list=[]
        self.volume_level=0
    def on(self):
        self.is_on=True
    def off(self):
        self.is_on=False
    def show_status(self):
        if self.is_on==False:
            print( 'Telewizor jest wyłączony')
        elif len(tv)>=self.channel_no:
            nr=self.channel_no-1
            print (f'Telewizor jest załączony, kanał {self.channel_no} ({self.channels_list[nr]}), poziom głośności: {self.volume_level}')
        else:
            print (f'Telewizor jest załączony, kanał {self.channel_no}, poziom głośności: {self.volume_level}')
    def set_channel(self,new_channel_no):
        self.channel_no=new_channel_no
    def set_channels(self,new_list):
        self.channels_list=new_list
    def show_channels(self):
        print ('Lista kanałow: ')
        for n in range(len(tv)):
            print (f'{n+1}. {self.channels_list[n]}')
    def __len__(self):
         return len(self.channels_list)
    def volume_up(self):
        if self.volume_level<10:
            self.volume_level+=1
        else:
            print('To jest maksymalny poziom glośności!')
    def volume_down(self):
        if self.volume_level>0:
            self.volume_level-=1
        else:
            print('To jest minimalny poziom glośności!')    
tv=TV()
tv.show_status()
tv.on()
tv.show_status()
tv.show_channels()
tab=['TVP1','TVP2','Polsat','TVN','Filmbox', 'Polsat 2','TVS']
tv.set_channels(tab)
tv.show_channels()
tv.show_status()
tv.off()

