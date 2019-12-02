# Compulsory Task 2

# Variable named weight to allow the user to enter their weight.
weight = input ("Please enter your weight in kg:")
weight = float (weight) # Used to cast the weight entered to a float.

# Variable named height to allow the user to enter their height.
height = input ("Please enter your height in m:")
height = float (height) # Used to cast the height entered to a float.

# Calculation used to determine the variable BMI value.
bmi = (weight)/(height*height)

# Elif statements using the calculated bmi to print out string based on the value.
if (bmi>=30):
    print ("You are obese.")
elif (bmi>=25):
    print("You are overweight.")
elif (bmi>=18.5):
    print ("Your weight is normal.")
elif (bmi<18.5):
    print ("You are underweight.")
    

