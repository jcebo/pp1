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

m = matrix.create(4,3)
matrix.print(m)
n=matrix.create2(3,4)
matrix.print(n)
l=matrix.create_unit(5)
matrix.print(l)