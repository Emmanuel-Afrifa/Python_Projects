# This code creates a table for the given sequence

# importing the necessary library
from tabulate import tabulate

data = [["Name", "Place", "Gender"], \
         ["Aman", "New Delhi", "Male"], ["Hritika", "New Delhi", "Female"], ["Krishna", "UP", "Male"]]

print(tabulate(data, headers='firstrow', tablefmt='fancy_grid'))