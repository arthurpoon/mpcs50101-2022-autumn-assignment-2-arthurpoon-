#Arthur Poon
#MPCS 50101 2,1 Intro to Programming Monday Section
#Problem 2

#ask for input score
str_score_input = input("Enter a score: ")

#convert string to float
if isinstance(float(str_score_input), float):
    float_score_input = float(str_score_input)
else:
    print("this is not a valid input")

#logic to check for positivity and whole numbers
if 0 <= float_score_input <= 100 and float_score_input % 1 == 0:

        #logic to match score to grades
        if 90 <= float_score_input <= 100:
            print(f"You received an A")
        elif 80 <= float_score_input <= 90:
            print(f"You received a B")
        elif 70 <= float_score_input <= 80:
            print(f"You received a C")
        elif 60 <= float_score_input <= 70:
            print(f"You received a D")
        else:
            print(f"You received a F")
else:
    print("That is not valid input. ")