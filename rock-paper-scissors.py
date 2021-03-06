# based on the tutorial at https: // realpython.com / python - rock - paper - scissors/

import random

possible_choices = ['rock', 'paper', 'scissors', 'lizard', 'spock']

victory_conditions = {
    'rock': ['scissors', 'lizard'],
    'paper': ['rock', 'spock'],
    'scissors': ['paper', 'lizard'],
    'lizard': ['paper', 'spock'],
    'spock': ['rock', 'scissors']
}

choices = str()
for i in range(0, len(possible_choices)):
    if i == len(possible_choices) - 1:
        choices += possible_choices[i].title()
    else:
        choices += possible_choices[i].title() + ', '


def ask_user_choice():
    choice = None
    while choice not in possible_choices:
        choice = input(f'Enter a choice ({choices}): ')
        choice = choice.lower().strip()
        if choice not in possible_choices:
            print('Choice not recognized!')
    return choice


def gen_computer_choice():
    choice = random.choice(possible_choices)
    return choice


def determine_winner(user_choice, computer_choice, win_record):
    defeats = victory_conditions[user_choice]

    if user_choice == computer_choice:
        print(f'You both chose {user_choice.title()}. It is a tie!')
        win_record[2] += 1
    elif computer_choice in defeats:
        print(f'{user_choice.title()} beats {computer_choice.title()}. You win!')
        win_record[0] += 1
    else:
        print(f'{computer_choice.title()} beats {user_choice.title()}. You lose!')
        win_record[1] += 1
    return win_record


win_counter = [0, 0, 0]  # win, lose, tie

while True:
    user_choice = ask_user_choice()

    computer_choice = gen_computer_choice()

    print(f'\nYou chose {user_choice.title()}, the computer chose {computer_choice.title()}.\n')

    determine_winner(user_choice, computer_choice, win_counter)

    print(f'\n{win_counter[0]} wins, {win_counter[1]} losses, {win_counter[2]} ties\n')

    keep_playing = input('Would you like to play again? (Y/N) ')
    if keep_playing.lower() in ['n', 'no']:
        break
    print('\n')
