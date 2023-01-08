import random


#if user != 'r' or user != 's' or user!= 'p':


def won(player, opponent):
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True


# if user == computer:
#         print("It's a tie. Let's Play again.")
# elif won(user, computer):
#         print("Congrats! You won.")
#         print(f"You chose {user} and the computer chose {computer}")
# else:
#         print("Sorry! You lost.")

def determine(player, opponent):
    if player == opponent:
        print("It's a tie. Let's play again")
    elif won(player,opponent):
        print("Congrats! You won.")
        print(f"You chose {player} and the computer chose {opponent}")
    else:
        print("Sorry! You lost")


user = input("What's your choice??? r = rock s = scissors p = paper\n")
computer = random.choice(['r', 's' , 'p'])

if user == 'r' or user == 'p' or user == 's':
    determine(user, computer)
else:
    print("Please choose one of the options given")
    quit()
