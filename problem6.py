#Arthur Poon
#MPCS 50101 2,1 Intro to Programming Monday Section
#Problem 6

#take input
input_text = input()

#take out all spaces:
input_text = input_text.replace(" ","")

#logic to check for pallindrome:
is_pallindrome = True
for index in range(0,len(input_text)-1):
    if input_text[index] == input_text[len(input_text)-index-1]:
        continue
    else:
        is_pallindrome = False

#print result

if is_pallindrome == True:
    print("This is a pallindrome.")
else:
    print("This is not a pallindrome.")
        

