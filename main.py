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

m1=[[5,5,0,1],[25,50,0,1],[25,50,0,1],[50,50,0,1],[50,50,0,1],[50,25,0,1],[50,25,0,1],[5,5,0,1]]
for i in range(2,15):
    draw_lines( m1, screen, color )
    color[2]=color[2]+30
    m1=[[5,5,0,1],[25,50,0,1],[25,50,0,1],[50,50,0,1],[50,50,0,1],[50,25,0,1],[50,25,0,1],[5,5,0,1]]
    m=[[i,0,0,0],[0,i,0,0],[0,0,1,0],[0,0,0,1]]
    matrix_mult(m,m1)

save_extension(screen, 'img.png')
display(screen)
