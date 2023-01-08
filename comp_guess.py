import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ''

    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        elif low == high:
            guess = low  #It could also be high because both numbers equal.

        feedback = input(f"Is {guess} too high (h), too low (l) or correct (c)??: ")
        if feedback == 'h':
            high = guess
            print("Sorry! Your guess is too high.")
        elif feedback == 'l':
            low = guess
            print("Sorry! Your guess is too low.")

    print(f"Congrats! You guessed {guess} correctly.")    

try:
    x = int(input("Enter the upper bound for the guess: "))
except (TypeError):
    print("Please enter an integer value.")
    quit()

computer_guess(x)