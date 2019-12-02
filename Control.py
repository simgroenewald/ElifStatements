# Compulsory Task 1

# Variable age to save the user's age once entered
age = input ("Please enter your age:")
age = int(age) # This is to cast the users input to an integer


# elif statement to print out strings based on the age the user has entered.
if (age >= 18):
    print ("You are old enough!")
elif (age >= 16):
    print ("Almost there.")
elif (age < 16):
    print ("You're just too young")
