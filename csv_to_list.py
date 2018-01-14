"""
Write a program which accepts a sequence of comma-separated numbers from console
and generate a list.
"""

import csv 

# Get user input into string
csv_numbers_string = input("Enter sequence of numbers in csv format :  ").strip()

# User csv library to parse csv file. Error if not in same format
csv_numbers_obj = csv.reader([csv_numbers_string])

# Convert to a list[lists] using csvreader functions
csv_numbers_list = list(csv_numbers_obj)

# Validate if list is populated correct
print ("Length of list : " , len(csv_numbers_list[0]))
print ("List contents entered : ", csv_numbers_list[0])


