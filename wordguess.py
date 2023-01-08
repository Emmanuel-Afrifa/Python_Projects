import random

take = input("Enter a sentence with the longest word having 5 characters: ")
take = take.split()

#generating random word
ran = random.choice(take)
guess = input("Guess the random word chosen from your sentence: ")


i = 0
for i in range(4):
    if guess != ran:
        print("Wrong guess!")
        guess = input("Guess the random word chosen from your sentence: ")
    elif guess == ran:
        print(f'The random word chosen was \'{ran}\'')
        print(f'Your guess is \'{guess}\'')
        print('Congrats!!!')
        quit()
        break

