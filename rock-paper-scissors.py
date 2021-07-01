import random


user_choice = input('Enter a choice (rock, paper, scissors): ')
user_choice = user_choice.lower()

possible_choices = ['rock', 'paper', 'scissors']

while user_choice not in possible_choices:
    print('Choice not recognised!')
    user_choice = input('Enter a choice (rock, paper, scissors): ')
    user_choice = user_choice.lower()

comp_choice = random.choice(possible_choices)

print(f'You chose {user_choice}, the computer chose {comp_choice}.\n')

if user_choice == comp_choice:
    print(f'You both chose {user_choice}. It is a tie!')
elif user_choice == 'rock':
    if comp_choice == 'scissors':
        print('Rock breaks Scissors. You win!')
    else:
        print('Paper wraps Rock. You lose!')
elif user_choice == 'paper':
    if comp_choice == 'rock':
        print('Paper wraps Rock. You win!')
    else:
        print('Scissors cuts Paper. You lose!')
else:   # scissors
    if comp_choice == 'paper':
        print('Scissors cuts Paper. You win!')
    else:
        print('Rock breaks Scissors. You lose!')
