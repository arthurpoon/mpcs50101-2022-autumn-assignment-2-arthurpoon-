#Arthur Poon
#MPCS 50101 2,1 Intro to Programming Monday Section
#Problem 7

def pyramid(height):
    length_of_row = 0
    while height > 0:
        length_of_row+=1
        print("*"*length_of_row)
        height-=1

input_height = int(input())
pyramid(input_height)
