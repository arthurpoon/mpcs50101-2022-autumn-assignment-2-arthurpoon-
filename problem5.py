#Arthur Poon
#MPCS 50101 2,1 Intro to Programming Monday Section
#Problem 5

#take input
input_number_string = input()

#check if input is a number 
if input_number_string.isnumeric():
    pass
else:
    print("that is not a valid number)")
    exit

#initiate sum and alternating sign
alternating_sum=0
alternating_sign = 1

#iteration logic, alternating sum
for digit in input_number_string:
    alternating_sum+=alternating_sign*int(digit)
    alternating_sign *= -1

#check if alternating sum is divisible by 11
if alternating_sum % 11 == 0:
    print("This is divisible by 11")
else:
    print("This is not divisible by 11")


