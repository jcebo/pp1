class song():
    def __init__(self,artist,title,album,year):
        self.artist=artist
        self.title=title
        self.album=album
        self.year=year
    def __str__(self):
        return 2*'\n' +'wykonawca: ' + ' '*(10-len('wykonawca')) + self.artist + '\n' + 'utwór: ' + ' '*(10-len('utwór')) + self.title + '\n' 'album: ' + ' '*(10-len('album')) + self.album + '\n' + 'rok: ' + ' '*(10-len('rok'))+ str(self.year)  
song1=song('dawid podiadlo', 'nic','mara',2015)
song2=song('kora','maslo','marcehw',1998)
song3=song('drake','violance','drama',1895)
print(song1,song2,song3)