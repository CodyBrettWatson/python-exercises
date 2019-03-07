# import functions_exercises as fe
# from functions_exercises import is_constant
# from functions_exercises import is_vowel as vowel

# print(fe.grade_converter(45))

# print(fe.is_constant('r'))

# print(fe.is_vowel('a'))


# import itertools

# def abc_123 (letters, numbers):
#     for r in range (1,3):
#         for s in itertools.product(letters, numbers,repeat=r):
#             print(''.join(s))

# print(abc_123('abc','123'))

# print(len(list(product('abc','123'))))
# print(list(product('abc','123')))

# def product(*args, repeat=1):
#     # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
#     # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
#     pools = [tuple(pool) for pool in args] * repeat
#     result = [[]]
#     for pool in pools:
#         result = [x+[y] for x in result for y in pool]
#     for prod in result:
#         yield tuple(prod)

# print (product('abc','123'))


# How many different ways can you combine two of the letters from "abcd"?

# from itertools import permutations

# print(list(permutations('abcd',2)))






# Total number of users
# Number of active users
# Number of inactive users
# Grand total of balances for all users
# Average balance per user
# User with the lowest balance
# User with the highest balance
# Most common favorite fruit
# Least most common favorite fruit
# Total number of unread messages for all users








from json import load
from collections import Counter


file = open('profiles.json', 'r')

file_data = load(file)

# def file_ids ():
#     for id in file_data: 
#         file_data_id = id['_id']  
#         print(file_data_id)


# def users_count():
#     ids_count = 0
#     for count in file_data:
#         if '_id' in count.keys():
#             ids_count +=1

#     print('Number of users:',ids_count)

# users_count()


print(len(file_data))