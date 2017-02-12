# First Draft of RPS project

#import random module for later use
import random
#import time module for print delay
import time


# def print_with_delay(input):
# 	print input, time.sleep(0.3)

def get_computer_choice():
	computer_choice = random.choice(['R','P','S'])
	return computer_choice

def get_beats_list(user_choice,computer_choice):
	beats_dict = {
		'R' : {
			'alias' : 'rock',
			'beats' : 'S',
			'ties' : 'R',
			'loses to' : 'P'

			},

		'P' : {
			'alias' : 'paper',
			'beats' : 'R',
			'ties' : 'P',
			'loses to' : 'S'
		},

		'S' : {
			'alias' : 'scissors',
			'beats' : 'P',
			'ties' : 'S',
			'loses to' : 'R'
		}
	}

	user_option_beats = beats_dict[user_choice]['beats']
	user_option_ties = beats_dict[user_choice]['ties']
	user_option_loses_to = beats_dict[user_choice]['loses to']
	user_option_alias = beats_dict[user_choice]['alias']

	computer_option_beats = beats_dict[computer_choice]['beats']
	computer_option_ties = beats_dict[computer_choice]['ties']
	computer_option_loses_to = beats_dict[computer_choice]['loses to']
	computer_option_alias = beats_dict[computer_choice]['alias']



	if user_choice == computer_option_loses_to:
		return 'You win!'
	elif user_choice == computer_option_beats:
		return 'The computer wins!'
	else:
		return "It's a tie!"



def get_user_choice():
	user_choice = str(raw_input('Welcome to Rock Paper Scissors!\nMake a choice: rock (R), paper (P) or scissors (S). ')).upper()

	if(user_choice in ('R','P','S')):

		return user_choice

	else:
		return ready


def main():
	ready = 1

	if(ready):
		user_choice = get_user_choice()
		computer_choice = get_computer_choice()

		beats_result = get_beats_list(user_choice, computer_choice)

		return "Your choice was %s.\n\nThe computer's choice was %s.\n\n%s" % (user_choice,computer_choice,beats_result)



print main()