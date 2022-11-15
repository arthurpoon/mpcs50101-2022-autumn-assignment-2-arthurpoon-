#Arthur Poon
#MPCS 50101 2,1 Intro to Programming Monday Section
#Problem 1

#ask for input temperature
str_temperature_input = input("Enter a temperature in Fahrenheit: ")

#convert string to float
    
try:
    float_temperature_input = float(str_temperature_input)
except:
    print("could not be converted to a float")


#logic to check for positivity and whole numbers
if float_temperature_input >= 0 and float_temperature_input % 1 == 0:
        celcius_temperature = round((float_temperature_input - 32) * 5/9 , 2)
        print(f"The temperature is {celcius_temperature} in Celsius.")
else:
    print("Please enter a positive, whole number numeric temperature.")
