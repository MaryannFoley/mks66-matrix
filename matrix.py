"""
A matrix will be an N sized list of 4 element lists.
Each individual list will represent an [x, y, z, 1] point.
For multiplication purposes, consider the lists like so:
x0  x1      xn
y0  y1      yn
z0  z1  ... zn
1  1        1
"""
import math

#print the matrix such that it looks like
#the template in the top comment
def print_matrix( matrix ):
    for i in range(4):
        strLine=""
        for list in matrix:
            strLine+=str(list[i])+"\t"
        print(strLine)

#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix ):
    for i in range(len(matrix)):
        for x in range(len(matrix)):
            if i == x:
                matrix[i][x]=1
            else:
                matrix[i][x]=0


#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    if len(m1[0])!=len(m2):
        print("can't multiply those")
        return
    for col in range(len(m1)):
        tempL=[]
        for val in m2[col]:
            tempL.append(val)
        for uh in range(len(m1)):
            sum=0
            for i in range(len(m1)):
                sum+=tempL[i]*m1[uh][i]
            m2[col][uh]=sum




def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
