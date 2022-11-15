#Arthur Poon
#MPCS 50101 2,1 Intro to Programming Monday Section
#Problem 4

def max_of_three(a,b,c):
    max = a
    if a > b and a > c:
        max = a
    elif b > a and b > c:
        max = b
    elif c > a and c > b:
        max = c
    print(max)
    return(max)


input_number1 = float(input())
input_number2 = float(input())
input_number3 = float(input())

max_of_three(input_number1,input_number2,input_number3)