import random
correctt = random.randint(1,100)
#print(correctt)

print('You have only 10 attempts')
try:
    guess = int(input("Enter an integer between 1 and 100: "))
except (ValueError, TypeError):
    print("Oops!! You entered a non-integer value. Run aagain and Input an integer!!!")
    quit()


#while True:
for i in range(9):
    if guess < correctt and guess > 0: 
        print("Your guess is too low")
        guess = int(input("Enter an integer between 1 and 100: "))
    elif guess > 100:
        print("The maximum value should be 100!!!")
        guess = int(input("Enter an integer between 1 and 100: "))
    elif guess < 1:
        print("The minimum value should be 1!!!")
        guess = int(input("Enter an integer between 1 and 100: "))
    elif guess > correctt and guess < 101:
        print("Your guess is too high")
        guess = int(input("Enter an integer between 1 and 100: "))
    elif guess == correctt:
        print(f'The random value generated was {correctt}')
        print(f'Your guess was {guess}')
        print("You're just right")
        break

print('You have exhausted all your 5 attempts!')
print(f'The random value generated was {correctt}')