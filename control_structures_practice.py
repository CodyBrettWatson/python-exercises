# 1. prompt the user for a day of the week, print out whether the day is Monday or not
# 2. prompt the user for a day of the week, print out whether the day is a weekday or a weekend
# 3. create variables for
#
# - the number of hour worked in one week
# - the hourly rate
# - how much the week's paycheck will be

# write the python code that calculates the weekly paycheck. You get paid time
# and a half if you work more than 40 hours

### exercise 1 ###
# weekday_prompt = input('What day of the week is it?')

# if weekday_prompt == 'Monday':
#     print('It is Monday')
# else:
#     print('It is not Monday')

### Exercise 2 ###

# weekday_prompt = input('What day of the week is it?').lower

# weekday_list = ['Saturday','Sunday']

# if weekday_prompt in weekday_list: 
#     print ('It is the weekend')
# else:
#     print('It is a weekday')

# 3. create variables for
#
# - the number of hour worked in one week
# - the hourly rate
# - how much the week's paycheck will be

# write the python code that calculates the weekly paycheck. You get paid time
# and a half if you work more than 40 hours

### Exercise 3 ###

# number_of_hours_worked = float(input('How many hours did you work this week? '))
# hourly_rate = float(input('What is your hourly rate? '))

# if number_of_hours_worked > 40:
#     weekly_paycheck = 40 * hourly_rate + (number_of_hours_worked - 40) * hourly_rate * 1.5
# else:
#     weekly_paycheck = hourly_rate * number_of_hours_worked

# print('You made','$', weekly_paycheck, 'this week!')


###____________Loops___________###


# for n in range (1,3):
#     print(n)



###__________Exercise 1__________###
# The input function can be used to prompt for input and use that input in your python code. 
# Prompt the user to enter a positive number and write a loop that counts from 0 to that number. 
# (Hints: first make sure that the value the user entered is a valid number, 
# also note that the input function returns a string, so you'll need to convert this to a numeric type.)
###__________Exercise 1__________###


# number = int(input('Enter a positive integer: '))

# for number_total in range(0, number):
#     print(number_total)


###_________Exercise 2__________###
#Write a program that prompts the user for a positive integer. 
#Next write a loop that prints out the numbers from the number the user entered down to 1.
###_________Exercise 2__________###

# number = int(input('Enter a positive integer: '))

# for number_total in reversed(range(1, number+1)):
#     print(number_total)

###_________Exercise 2__________###

###_________Exercise 2__________###


# i=5

# while i <= 15:
#     print (i)
#     i += 1


# Create a while loop that will count by 2's starting with 0 and ending at 100. 
# Follow each number with a new line.

# i=0

# while i <= 100:
#     print (i)
#     i += 2


# i=100

# while i >= -10:
#     print (i)
#     i -= 5

# Create a while loop that starts at 2, 
# and displays the number squared on each line while the number is less than 1,000,000. 
# Output should equal:

# i=2

# while i <= 1000000:
#     print (i)
#     i *= i

#Write a loop that uses print to create the output shown below.
i=100

while i >= 5:
    print (i)
    i -= 5