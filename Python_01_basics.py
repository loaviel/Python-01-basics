
#Exercise 1:
print("Exercise 1")
#Write a line of code in Python that prints 'Hello World' to the screen.


print("Hello World")


print("\nExercise 2")
#Exercise 2:
#Now declare a variable called name. Assign your firstname as the value for this variable. Print this value to the screen to check that it has been assigned to the variable.
name = "kristiyan"
print(name)


print("\nExercise 3")
#Exercise 3:
#Now declare two variables. Assign the value 10 to the first variable. Then assign the value 40 to the second variable. Then add the variables together and print out the result.
firstValue = 10
secondValue = 40
totalValue = firstValue + secondValue
print(totalValue)


print("\nExercise 4")
#Exercise 4:
#Providing you have completed the previous two exercises, you should have three variables with assigned values. Now write code in the cell below which will print out the individual values for these variables declared previously. In terms of formatting, print out one value for each line. You could use the '\n' escape character for a 'new line'
#Note: You won't need to re-declare these variables as the values should still be stored in memory until the session is closed.
print(name, "\n", firstValue, "\n", secondValue)

print("\nExercise 5")
#Exericse 5:
#Now use a function in Python to ask the user to enter their name. This name should be stored in an appropriate variable. Once stored, print the value of this variable (what the user entered) to the screen.
def welcome():
    username = input("Enter name:")
    print("Hello " + username)
    
welcome()


print("\nExercise 6")
#Exercise 6:
#Now ask the user to enter two numbers, and store these inputs in two variables. Once stored, print out the average of the two numbers.
#Hint: If you get stuck, first check which type of data is being returned from the Python function.
def returnAverage():
    firstNumber = int(input("Enter first number: "))
    secondNumber = int(input("Enter second number: "))
    averageNumber = (firstNumber + secondNumber) / 2
    print(averageNumber)
    
returnAverage()

print("\nExercise 7")
#Exercise 7:
#Design a program that asks the user to enter values for the length and height of a rectangle and then outputs the perimeter and area of the rectangle to the screen.
#Extension: ask the user to also type in a unit: cm, m, inches etc. Include this unit in the output.

def returnRectangle():
    height = float(input("Enter height of rectangle: "))
    length = float(input("Enter length of rectangle: "))
    
    

print("\nExercise 8")
print("\nExercise 9")
print("\nExercise 10")
print("\nExercise 11")
print("\nExercise 12")
print("\nExercise 13")
print("\nExercise 14")
print("\nExercise 15")