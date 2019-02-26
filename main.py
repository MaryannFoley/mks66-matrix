from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()
A = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
B = [[11,12,13,14],[15,16,17,18],[19,20,21,22],[23,24,25,26]]
matrix_mult(A,B)
print_matrix(A)
print("--------------")
print_matrix(B)
matrix_mult(B,A)
print("--------------")
print_matrix(A)
print("--------------")
print_matrix(B)
print("--------------")
aCopy=[]
for i in A:
    tempL=[]
    for j in i:
        tempL.append(j)
    aCopy.append(tempL)
matrix_mult(aCopy,A)
print_matrix(A)

m1=[[0,0,0,1],[5,10,0,1],[10,10,0,1],[10,5,0,1]]

draw_lines( m1, screen, color )
save_extension(screen, 'img.png')
display(screen)
