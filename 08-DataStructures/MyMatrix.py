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
        
    

m = matrix.create(4,3)
matrix.print(m)
n=matrix.create2(3,4)
matrix.print(n)
l=matrix.create_unit(5)
matrix.print(l)
t=matrix.create2(5,3)
matrix.fill_random(t,5,9)
matrix.print(t)
z=matrix.create2(5,3)
matrix.fill_random(z,1,9)
matrix.print(z)
matrix.transponse(z)
