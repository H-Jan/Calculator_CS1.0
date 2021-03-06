
print("Calculator!")

number1 = float(input("First number: "))
number2 = float(input("Second number: "))
print("Addition")
print("Solution: ", number1 + number2)
#This first action is taking the defined numbers and simply adding them. 
#Float was used to ensure that should the user input a decimal or whole number, both operations would work

print("Subtraction")
print("Solution: ", number1 - number2)
# This action is taking the previously defined variables, number1 and number2, and printing out the subtraction mathematics
# It is first printing out the "Subtraction" string to indicate to the user which operation is being performed 
# It then outputs the "Solution" string to indicate the answer

print("Multiplication")
print("Solution: ", number1 * number2)
# This line of code is taking the previously defined variables, number1 and number2, and outputting the multiplation mathematics
# It is first printing out the "Multiplication" string to indicate to the user which operation it is performing
# Followed by the "Solution" string to indicate the answer 

print("Division")
print("Solution: ", number1 / number2)
# This line of code is taking the previously defined number variables, number1 and number2, and outputting the divison operation
# Since this is a given command in Python, it is done through simply including the slash between the two numbers
# Before the operation, we are outputting the string "Division" to direct the user as to what operation is happeining
# We are also outputting the string "Solution" followed by the operation itself to yield both the answer and direct the user to the answer

print("Remainder")
remainder = (number1 % number2)
print("The remainder of ", number1, " divided by ", number2, " is ", remainder)
# This sequence of code it first returning a string called "Remainder" to demonstrate to the user the operation made
# It is taking the float variables and inputting them into the built-in operation fmod which is defined under the string "remainder"
# This is then returned through the string "The remainder of (number1) divided by (number2) is (remainder) to be more user friendly

print("Percentage")
percentage = ((number1/100) * number2)
print("Solution: ", number1, " percent of ", number2, " equals ", percentage)
#In this sequence of code, we are first printing the string "Percentage"
# We are then defining the operations for yielding a percentage, using previously defined variables number1 and number2
# To define this operation, we simply divide number1 by 100, and multiply the result by number2, which is done in order through the order of operations using parethesis
# Then, to make it easier for our user, we are printing the string "Solution" followed by the number, another string defining the percentage we took, and the result

print("Power Function")
power = pow(number1, number2)
print("Solution: ", number1, " to the power of ", number2, " equals ", power)
#In this sequence of code, we are first printing the "Power Function" string to indicate to the user what operation is being performed
#Them we are defining power as a mathematical operation involving our two float variables
#Lastly, we are implementing a string statement in the print function to return to the user a clear and concise manner of what is being done
# We are as well implementing our defined power sequence

print("Average")
average = ((number1 + number2) / 2)
print("Solution: The average of ", number1, " and ", number2, " is ", average)
# In this sequence, we are printing the string "Average" to indicate to the user what operation is being performed
# We are then taking out defined float variables and inputting them into the average formula used
# Lastly, we are implementing the string statement to indicate the answers derived from the average formula used













