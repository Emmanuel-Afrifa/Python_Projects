import math

# Creating a class to store the student attributes and methods
class Student:
    def __init__(self, firstname, lastname, age, grade):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.grade = grade


    def __str__(self):
        return f'My name is {self.firstname} {self.lastname}, {self.age} years of age and had a mark of {self.grade}'

    def warning(self):
        if self.age > 15 and self.grade < 40:
            print(f'Hey {self.firstname} {self.lastname}, You better sit up and learn. You had a mark of {self.grade}\n')
    
    # Defining a function that grades the students
    def grader(self):
        """This function grades the students"""
        if self.grade < 40 and self.grade >= 0:
            print('Sorry!!! You failed. You have to sit up and learn')
        elif self.grade >= 40 and self.grade <60:
            print('You had grade C. More room for improvement')
        elif self.grade >=60 and self.grade < 70:
            print('You had grade B. Keep it up')
        elif self.grade >= 70 and self.grade <= 100:
            print('Excellent!!! You had grade A')
        

# Instantiating 6 students
s1 = Student('Emma','Cain',19,86)
s2 = Student('Anna','Michaels',14,66)
s3 = Student('Daniel','Craig',20,75)
s4 = Student('Bernard','Watson',15,37)
s5 = Student('Candy','Dolce',18,58)
s6 = Student('Ama','Bismark',22,33)


studs = [s1,s2,s3,s4,s5,s6]

for student in studs:
    student.warning()
    

# Saving the firstnames of the students as a list
firstname = [first.firstname for first in studs]

# Saving the firstnames of the students as a list
lastname = [last.firstname for last in studs]

# Finding the average age of the students printing the resuls
ages = [age.age for age in studs]
average_age = sum(ages)/len(ages)
print(f'The average age of the students is {average_age:.2f}\n')


# finding the average, maximum and minimum grades of the students prnting the results
# Minimum grade
grades = [der.grade for der in studs]
min = 100
for item in grades:
    if item < min:
        min = item

print(f'The minimum grade if the students is {min:.2f}\n')

# Maximum grade
max = 0
for item in grades:
    if item > max:
        max = item

print(f'The maximum grade if the students is {max:.2f}\n')

# Average grade
average_grade = sum(grades)/len(grades)
print(f'The average grade of the students is {average_grade:.2f}\n')

# printing the ful details of students with the letter 'a' in their name
for item in studs:
    if 'a' in item.firstname or 'a' in item.lastname:
        print(item)

