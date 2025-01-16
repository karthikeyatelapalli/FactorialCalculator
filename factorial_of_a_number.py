# Description
# Factorial of a number 
'''This straightforward Python program uses a while loop to get the factorial of a given non-negative integer. The program asks the user
 to enter an integer that is not negative and then verifies the input to make sure the value entered is not negative. The software keeps 
 requesting a non-negative integer if the input is negative until a valid input is provided. The software utilizes a while loop to get the
 supplied number's factorial after determining if  the input is valid. The program multiplies each non-negative integer from
 1 to n in order to calculate the factorial. The outcome is then shown using comma separation.'''
# It takes the input from the user
number = int(input("Enter a nonnegative integer: "))

# Checks if the input is a nonnegative number or not
while number < 0:
    number = int(input("Enter a nonnegative integer: "))

# Now it calculates the factorial for the number
factorial = 1
i = 1
while i <= number:
    factorial *= i
    i += 1

# Now finally it prints the result 
print("The factorial of", number, "is", "{:,}".format(factorial))
