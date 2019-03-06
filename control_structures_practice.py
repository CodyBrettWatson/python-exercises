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
# i=100

# while i >= 5:
#     print (i)
#     i -= 5

# Write some code that prompts the user for a number, 
# then shows a multiplication table up through 10 for that number. 

# 7 x 1 = 7
# 7 x 2 = 14
# 7 x 3 = 21

# for i in range(1, 10):
#     print("i =", i, ":", end=" ")
#     for j in range(1, 10):
#         print("{:2d}".format(i * j), end=" ")
#     print()




# number = int(input('pick a number:'))

# for multiply_by in range(1, 11):
#     print ("{:2d}".format(number), 'x', "{:2d}".format(multiply_by), '=', "{:2d}".format((number * multiply_by)))


# Create a for loop that uses print to create the output shown below.
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
# 88888888
# 999999999

# for i in range(10):
#     print(str(i)*i)



# for desc_digits in range (1,10):
#     print(str(desc_digits)*desc_digits)
    #make this out put as a pyramid shape
    #make this out put as a leaning tower of lyre




# Prompt the user for an odd number between 1 and 50. 
# Use a loop and a break statement to continue prompting the user if they enter invalid input. 
# (Hint: use the isdigit method on strings to determine this). 
# Use a loop and the continue statement to output all the odd numbers between 1 and 50, except for the number the user entered.

# skip_number = int(input('Pick an odd number between 1 and 50: '))

# print('Number to skip is: ',skip_number)
# for odd_number in range(1,50):
#     if odd_number % 2 != 0 and odd_number != skip_number:
#         print('Here is an odd number: ', odd_number)    
#     if odd_number == skip_number:
#         print('Yikes! Skipping number: ', odd_number)


# The input function can be used to prompt for input and use that input in your python code. 
# Prompt the user to enter a positive number and write a loop that counts from 0 to that number. 
# (Hints: first make sure that the value the user entered is a valid number, also note that the input function returns a string,
# so you'll need to convert this to a numeric type.)

# number = int(input('Pick a positive number: '))

# for loop in range(0, number+1):
#     print (loop)
#     loop += 1



#FIZZBUZZ
# Write a program that prints the numbers from 1 to 100.
# For multiples of three print "Fizz" instead of the number
# For the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".

# for numbers in range (1,101):
#     if numbers %3 ==0 and numbers %5 ==0:
#         print('FizzBuzz')
#     elif numbers %3 == 0:
#         print('Fizz')
#     elif numbers %5 == 0:
#         print('Buzz')
#     else:
#         print(numbers)


#########Display a table of powers##########

# Prompt the user to enter an integer.
# Display a table of squares and cubes from 1 to the value entered.
# Ask if the user wants to continue.
# Assume that the user will enter valid data.
# Only continue if the user agrees to.

# What number would you like to go up to? 5

# Here is your table!

# number | squared | cubed
# ------ | ------- | -----
# 1      | 1       | 1
# 2      | 4       | 8
# 3      | 9       | 27
# 4      | 16      | 64
# 5      | 25      | 125



# def square_cube_table():
#     user_input = int(input('Enter an integer:'))
#     createTable(user_input)

# def createTable(max):
#     print ("{:5s}".format('number'),'|', 
#     "{:5s}".format('square'),'|', 
#     "{:5s}".format('cube'))
#     print ("{:5s}".format('-'*len('number')),'|', 
#     "{:5s}".format('-'*len('square')),'|', 
#     "{:5s}".format('-'*len('cube')))
#     for x in range (1, max+1):
#        tableLine(x)
#     continueGoing(x)
    
# def continueGoing(last):
#     next = last
#     userInput = input('Continue? ')
#     if userInput == 'y':
#         square_cube_table()
#         createTable(next)
#         continueGoing(next)
#     else:
#         exit()
        
# def tableLine(x): 
#      print ("{:6s}".format('%2d' % (x)),'|', 
#         "{:6s}".format('%2d' % (x**2)),'|',
#         "{:6s}".format('%2d' % (x**3)))

# square_cube_table()


# Convert given number grades into letter grades.

# Prompt the user for a numerical grade from 0 to 100.
# Display the corresponding letter grade.
# Prompt the user to continue.
# Assume that the user will enter valid integers for the grades.
# The application should only continue if the user agrees to.
# Grade Ranges:

# A : 100 - 88
# B : 87 - 80
# C : 79 - 67
# D : 66 - 60
# F : 59 - 0


# def grade_converter ():
#     grade_number = int(input('What was your grade percentage?'))

#     if grade_number in range (0,60):
#         print('F')
#     if grade_number in range (60,67):
#         print('D')
#     if grade_number in range (67,80):
#         print('C')
#     if grade_number in range (80,88):
#         print('B')    
#     if grade_number in range (88,101):
#         print('A')

#     while True:
#         if input('Continue?') == 'y'.upper or 'yes'.upper:
#             grade_converter()
#         elif input('Continue?') == 'n'.upper or 'no'.upper:
#             break

# grade_converter()



#######DICTIONARIES########
# Create a list of dictionaries where each dictionary represents a book that you have read. 
# Each dictionary in the list should have the keys title, author, and genre. 
# Loop through the list and print out information about each book.

# Prompt the user to enter a genre, then loop through your books list and print out the titles of all the books in that genre.


books_dict = [{"Author": "Dan Brown", "Title":"Deception Point", "Genre":"Thriller"},
{"Author":"Karl Marx", "Title":"Communist Manifesto", "Genre":"Non-Fiction"},
{"Author":"Miguel de Cervantes", "Title":"Don Quixote", "Genre":"Fiction"},
{"Author":"Uknown", "Title":"Gilgamesh", "Genre":"Epic Poem"},
{"Author":"Confucius", "Title":"The Analects", "Genre":"Philosophy"},
{"Author":"Unkown", "Title":"Popol Vuh", "Genre":"Mythology"}
]

def book_facts ():
    for 