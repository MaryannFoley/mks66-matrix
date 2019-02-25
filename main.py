from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()
A = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
B = [[11,12,13,14],[15,16,17,18],[19,20,21,22],[23,24,25,26]]
print_matrix(A)
#matrix_mult(A,B)
print_matrix(A)
print("Still debugging")
draw_lines( matrix, screen, color )
display(screen)
