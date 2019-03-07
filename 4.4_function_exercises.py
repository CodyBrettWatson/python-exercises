# Define a function named is_two. 
# It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.

# def is_two (x):
#     if x == 2 or x == '2':
#         return True

# print(is_two(2))


# Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.

def is_vowel(letter):
    if letter in ('a','e','i','o','u'):
        return True
    elif letter in 'y':
        return 'sometimes' 
    else:
        return False

# print(is_vowel('a'))
# print(is_vowel('y'))

# Define a function named is_consonant. 
# It should return True if the passed string is a consonant, False otherwise. 
# Use your is_vowel function to accomplish this.

def is_constant (letter):
    if is_vowel(letter):
        return False
    else:
        return True

# print(is_constant('g'))
# print(is_constant('a'))

# Define a function that accepts a string that is a word. 
# The function should capitalize the first letter of the word if the word starts with a consonant.

def accept_string(word):
    if word [0] not in ['a','e','i','o','u']:
        return word.capitalize()

# print(accept_string('bob'))

# Define a function named calculate_tip. 
# It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.

def calculate_tip (tip_percentage, bill_total):
        return tip_percentage * bill_total

# print(calculate_tip(.1, 34))

# Define a function named apply_discount. 
# It should accept an original price, and a discount percentage, and return the price after the discount is applied.

def apply_discount (original_price, discount_percentage):
    return original_price - (original_price * discount_percentage)

# print(apply_discount(34, .1))

# Define a function named handle_commas. 
# It should accept a string that is a number that contains commas in it as input, and return a number as output.

def handle_functions(comma):
    without = comma.replace(',','')
    return without

# print(handle_functions('However, you are a clod!'))
# print(handle_functions('1,000,000'))

# Define a function named get_letter_grade. 
# It should accept a number and return the letter grade associated with that number (A-F).

def grade_converter (grade_number):
    if grade_number in range (0,60):
        return 'F'
    if grade_number in range (60,67):
        return 'D'
    if grade_number in range (67,80):
        return 'C'
    if grade_number in range (80,88):
        return 'B'    
    if grade_number in range (88,101):
        return 'A'

# print(grade_converter(54))

# Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.

def remove_vowels(word):
    word_list =[]
    for v in word:
        if is_vowel(v):
            continue
        word_list.append(v)
    return ''.join(word_list)

# def remove_vowels (a_string):
#     return ''.join([letter for letter in a_string if not is_vowel(letter)])

# def remove_vowels (string):
#     for a vowel in 'aeiou':
#         string = string.replace()
#     return string


# Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
# anything that is not a valid python identifier should be removed
# leading and trailing whitespace should be removed
# everything should be lowercase
# spaces should be replaced with underscores
# for example:
# Name will become name
# First Name will become first_name
# % Completed will become completed
import re

LETTERS = re.search("[a-z]") #constant

def normalize_name(a_string):
    a_string = a_string.strip().lower()  #method chaining
    valid_characters = []
    for character in a_string:
        if character in LETTERS:
            valid_characters.append(character)
    return ''.join(valid_characters).strip().replace(' ', '_')

print(normalize_name('Name'))
print(normalize_name('First Name'))
print(normalize_name('% Completed'))

# print('\n'*3)

# Write a function named cumsum that accepts a list of 
# numbers and returns a list that is the cumulative sum of the numbers in the list.
# cumsum([1, 1, 1]) returns [1, 2, 3]
# cumsum([1, 2, 3, 4]) returns [1, 3, 6, 10]


# def cumsum(numbers):
#     sums = [numbers[0]]
#     for current_number in numbers[1:]:
#         last_number = sums[-1]
#         next_number = last_number + current_number
#         sums.append(next_number)
#     return sums

# print(cumsum([1,1,1]))
# print(cumsum([1,2,3]))
# print(cumsum([1,2,3,4]))