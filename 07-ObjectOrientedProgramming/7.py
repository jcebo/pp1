class Student():
    college='UEK Kraków'
    album_no=100000
    def __init__(self,fname,lname,degree):
        self.fname=fname
        self.lname=lname
        self.degree=degree       
        self.album=Student.album_no
        Student.album_no+=1
    def __str__(self):
        return f'{self.fname} {self.lname} ({self.album}), {self.degree}, {Student.college}\n'
        
    
student1=Student('Maciej','Murak','Ogrodnictwo')
student2=Student('Waleria','Por','mAtematyka')
student3=Student('Rumek','Rorea','Informatyka Stosowana')
print(student1,student2,student3)

