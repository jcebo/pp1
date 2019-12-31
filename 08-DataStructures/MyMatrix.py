from random import randint
class matrix():
    @staticmethod
    def create(x,y):
        matrix = []
        value = 0
        for i in range(x):
            # create single row
            row = []
            for j in range(y):
                row.append(value)
            # add row to matrix
            matrix.append(row)
        return matrix
    @staticmethod
    def create2(w,h):
        matrix=[[0 for n in range(w)] for k in range(h)]
        return matrix
    @staticmethod
    def create_unit(x):
        m=matrix.create2(x,x)
        for n in range(len(m)):
            m[n][n]=1
        return m

    @staticmethod
    def print(matrix):
        for row in matrix:
            print(row)
    @staticmethod
    def fill_random(matrix,m,n):
        for i in range(len(matrix)):
            for x in range(len(matrix[i])):
                matrix[i][x]=randint(m,n)
    @staticmethod
    def transponse(mat):
        h=len(mat)
        w=len(mat[0])
        a=matrix.create2(h,w)
        for n in range(len(a)):
            for i in range(len(a[n])):
                a[n][i]=mat[i][n]
        matrix.print(a)
    @staticmethod
    def create_diagonal(x,m,n):
        mat=matrix.create2(x,x)
        for x in range(len(mat)):
            mat[x][x]=randint(m,n)
        return mat
    @staticmethod
    def compare(matrix1,matrix2):
        licznik=0
        if len(matrix1)==len(matrix2):
            for n in range(len(matrix1)):
                if matrix1[n]==matrix2[n]:
                    licznik+=0
                else:
                    licznik+=1
        if licznik==0 and len(matrix1)==len(matrix2):
            return "Macierze mają takie same wymiary i ich wartości są takie same"                    
        elif len(matrix1)!=len(matrix2):
            return "Macierze maja różne wymiary"
        else:
            return "Macierze nie mają takich samych wartości"
        
        
m = matrix.create(4,3)
matrix.print(m)
print('\n')
n=matrix.create2(3,4)
matrix.print(n)
print('\n')
l=matrix.create_unit(5)
matrix.print(l)
print('\n')
t=matrix.create2(5,3)
matrix.fill_random(t,5,9)
matrix.print(t)
print('\n')
z=matrix.create2(5,3)
matrix.fill_random(z,1,9)
matrix.print(z)
print('\n')
matrix.transponse(z)
print('\n')
zad21=matrix.create_diagonal(5,10,50)
matrix.print(zad21)