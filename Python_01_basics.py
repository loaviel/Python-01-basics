from datetime import datetime, timedelta


print("Exercise 1")
#Exercise 1:
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
print(f"The sum of {firstValue} and {secondValue} is {totalValue}.")


print("\nExercise 4")
#Exercise 4:
#Providing you have completed the previous two exercises, you should have three variables with assigned values. Now write code in the cell below which will print out the individual values for these variables declared previously. In terms of formatting, print out one value for each line. You could use the '\n' escape character for a 'new line'
#Note: You won't need to re-declare these variables as the values should still be stored in memory until the session is closed.


print(f"Name: {name}")
print(f"First Value: {firstValue}")
print(f"Second Value: {secondValue}")

print("\nExercise 5")
#Exericse 5:
#Now use a function in Python to ask the user to enter their name. This name should be stored in an appropriate variable. Once stored, print the value of this variable (what the user entered) to the screen.


def welcome():
    username = input("Enter name:")
    print(f"Hello, {username}")
    
welcome()


print("\nExercise 6")
#Exercise 6:
#Now ask the user to enter two numbers, and store these inputs in two variables. Once stored, print out the average of the two numbers.
#Hint: If you get stuck, first check which type of data is being returned from the Python function.
def returnAverage():
    firstNumber = float(input("Enter first number: "))
    secondNumber = float(input("Enter second number: "))
    averageNumber = (firstNumber + secondNumber) / 2
    print(f"The average of {firstNumber} and {secondNumber} is {averageNumber}.")
    
returnAverage()

print("\nExercise 7")
#Exercise 7:
#Design a program that asks the user to enter values for the length and height of a rectangle and then outputs the perimeter and area of the rectangle to the screen.
#Extension: ask the user to also type in a unit: cm, m, inches etc. Include this unit in the output.

def returnRectangle():
    height = float(input("Enter height of rectangle: "))
    length = float(input("Enter length of rectangle: "))
    unit = input("Enter the unit (e.g., cm, m, inches): ")
    
    perimeter = 2 * (height + length)
    area = height * length
    
    print(f"\nThe perimeter of the rectangle is {perimeter} {unit}.")
    print(f"The area of the rectangle is {area} square {unit}.")
    
returnRectangle()

print("\nExercise 8")
#Exercise 8:
#Write a script that will convert miles to feet. First ask the user to enter a quantity of miles. Store this in an appropriate variable. Then convert and output (print) the number of feet to the screen. Test this for a number of inputs to check the conversion works correctly.
#For reference, there are 5280 feet in 1.0 mile.
#Extension: Also ask the user to enter the same number of feet and check this converts back to the original number of miles.

def returnMilesToFeet():
    milesInput = float(input("Enter the number of miles: "))
    feetConverted = milesInput * 5280
    
    print(f"{milesInput} miles is equal to {feetConverted} feet.")
    feetInput = float(input("Enter the conversion result you were shown: "))
  
    milesConverted = feetInput / 5280
    print(f"{feetInput} feet is equal to {milesConverted} miles.")

returnMilesToFeet()



print("\nExercise 9")
#Exercise 9:
#Write a program that will calculate the how much interest will paid on money invested in a savings account. Select an appropriate interest rate (based on the current markets at time of reading) and consider how you will represent this in your program. The user should enter the deposit amount and the program should display how much money the user will have after the interest is paid at the end of the year.
#Extension: Think about the appropriate formatting for currency. For example, consider how to print the output with two decimal places for pound sterling.

def calculateInterest():
    interestRate = 0.05  #5% looks normal in sept 2024
    depositAmount = float(input("Enter the deposit amount: "))
    interestEarned = depositAmount * interestRate
    totalAmount = depositAmount + interestEarned
    print(f"After one year, you will make: £{totalAmount:.2f}")

calculateInterest()


print("\nExercise 10")
#Exercise 10:
#Ask the user to enter the month that they were born in. Calculate how many months it will be until their next birthday.
#For simplicity, it would be easier if they enter this in the format of an integer (int). For example, May would be the 5th month of the year.
#Challenge: Instead of asking for integers, ask the user to enter their month of birth as a string (str)!

def monthsUntilNextBirthday():
    monthNames = ["January", "February", "March", "April", "May", "June", 
                  "July", "August", "September", "October", "November", "December"]
    
    birthMonth = input("Enter the month you were born in (September / December / etc.): ").capitalize()
    currentMonth = input("Enter the current month: ").capitalize()
    
    if currentMonth in monthNames and birthMonth in monthNames:
        currentMonthIndex = monthNames.index(currentMonth)
        birthMonthIndex = monthNames.index(birthMonth)
        monthsUntilNext = (birthMonthIndex - currentMonthIndex) % 12
        print(f"Your birthday is in {monthsUntilNext} months.")
    else:
        print("Invalid month. Please enter the full month's name.")

monthsUntilNextBirthday()

print("\nExercise 11")
#Further to the previous exercise, write some code that asks the user to enter their date of birth (DOB).
#Now calculate how old the user is from their date of birth and output this to the screen.


def calculateAge():
    birthYear = int(input("Enter the year you were born: "))
    currentYear = int(input("Enter the current year: "))
    
    age = currentYear - birthYear
    print(f"You are {age} years old.")
    
    return birthYear

birthYear = calculateAge()

print("\nExercise 12")
#(Bonus) Exercise 12:
#Extend the previous exercise to calculate how many days it is until the user's next birthday from the DOB entered.
#Extension: Check whether this is a leap year, and if it is, remember to make an adjustment.

def calculateDaysUntilNextBirthday(birthYear):
    birthMonth = int(input("Enter the month you were born (1-12): "))
    birthDay = int(input("Enter the day you were born: (1-31): "))
    
    currentDate = datetime.now()
    nextBirthday = datetime(currentDate.year, birthMonth, birthDay)
    
    if nextBirthday < currentDate:
        nextBirthday = datetime(currentDate.year + 1, birthMonth, birthDay)
        
    daysUntilNextBirthday = (nextBirthday - currentDate).days
    
    print(f"There are {daysUntilNextBirthday} days until your next birthday.")
    
calculateDaysUntilNextBirthday(birthYear)
    
print("\nExercise 13")
#(Bonus) Exercise 13:
#Write a script which will process the user's DOB and output which day of the week they were born.


def getBirthDay():
    DOB = input("Enter your date of birth (YYYY-MM-DD): ")
    
    DOBStrip = datetime.strptime(DOB, "%Y-%m-%d")
    
    dayOfWeek = DOBStrip.strftime("%A")
    
    print(f"You were born on a {dayOfWeek}.")

getBirthDay()

print("\nExercise 14")
#Bonus) Exercise 14:
#Define a function called 'get_input'. The function should prompt the user to enter an input and then return this to the calling location. Test this works by calling the function a few times, prompting the user for different types of data.
#Extension 1: You may wish to extend this further to create a separate function which will 'get' (return) integers. This would be a separate function from the 'get_input' function, which would by default return strings (str).
#Extension 2: You may wish to incorporate this function into the scripts which process the user's DOB.


def getInput(prompt):
    return input(prompt)

def getInteger(prompt):
    userInput = getInput(prompt)
    return int(userInput) if userInput.isdigit() else None


def processDob():
    birthYear = getInteger("Enter the year you were born (e.g., 2000): ")
    birthMonth = getInteger("Enter the month you were born (1-12): ")
    birthDay = getInteger("Enter the day you were born (1-31): ")

    if None in (birthYear, birthMonth, birthDay):
        print("Invalid input. Please enter numeric values for year, month, and day.")
        return

    birthDate = datetime(birthYear, birthMonth, birthDay)
    dayOfWeek = birthDate.strftime("%A")

    print(f"You were born on a {dayOfWeek}.")

    # TESTING 
    
name = getInput("Enter your name: ")
print(f"Hello, {name}!")

favoriteNumber = getInteger("Enter your favorite number: ")
if favoriteNumber is not None:
    print(f"Your favorite number is {favoriteNumber}.\n")
else:
    print("Invalid favorite number input.\n")


processDob()
    


print("\nExercise 15")

#(Bonus) Exercise 15:
#Continuing from the previous exercise, can you add conditional statements that will evaluate whether the input is 'valid'. 
#For example, if the user was asked to type in their date of birth, check to see whether this is the format required (this could be DD/MM/YYYY). 
#Output a message to prompt the user if the format entered is not to the program's specification.

def validateDateFormat(dateStr):
    try:
        datetime.strptime(dateStr, "%d/%m/%Y")
        return True
    except ValueError:
        return False
    
def processDobImproved():
    while True:
        birthDateStr = getInput("Enter your date of birth (DD/MM/YYYY): ")
        if validateDateFormat(birthDateStr):
            break
        else:
            print("Invalid format. Please enter your date of birth in DD/MM/YYYY format.")

    birthDate = datetime.strptime(birthDateStr, "%d/%m/%Y")
    dayOfWeek = birthDate.strftime("%A")
    print(f"You were born on a {dayOfWeek}.")
    
processDobImproved()